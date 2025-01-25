from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Contact
from .utils import format_response, get_email_if_contact_exists, paginate_data
from spam.utils import get_spam_likelihood
from user.models import User
from urllib.parse import unquote
from django.core.cache import cache

class SearchByName(APIView):
    """
    This view allows an authenticated user to search the global database for
    users or contacts whose names match the given query. The results include Registered users,
    Contacts associated with any user.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        query_name = request.query_params.get('query',None)

        if not query_name:
            return Response({"error": "Query param name is required."}, status=400)

        #fetching from cache
        cache_key = f'name={query_name}'
        search_results = cache.get(cache_key)

        if not search_results:
            #quering from db
            search_results = []
            users = User.objects.filter(name__icontains=query_name) #registered users
            contacts = Contact.objects.filter(name__icontains=query_name).only('name','phone')

            for user in users:
                email = get_email_if_contact_exists(user, request.user.phone)
                search_results.append(format_response(user.name, user.phone, get_spam_likelihood(user.phone), email))

            search_results += [format_response(contact.name, contact.phone, get_spam_likelihood(contact.phone)) for contact in contacts]

            #caching results for 5 min
            cache.set(cache_key,search_results,timeout=300)

        #paginating results
        page_number = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 4)
        return paginate_data(page_number,page_size,search_results)

class SearchByPhone(APIView):
    """
    This view allows an authenticated user to search the global database for
    users or contacts or spams whose phone numbers match the given query.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self, request):
        query_phone = request.query_params.get('query', None)

        if not query_phone:
            return Response({"error": "Query param phone is required."}, status=400)
        #decoding phone number
        query_phone = unquote(query_phone)

        #fetching from cache
        search_results = cache.get("phone=" + query_phone)

        if not search_results:
            #quering database
            search_results = []
            user = User.objects.filter(phone=query_phone).first()

            if user:
                email = get_email_if_contact_exists(user, request.user.phone)
                search_results.append(format_response(user.name, user.phone, get_spam_likelihood(user.phone), email))
            else:
                contacts = Contact.objects.filter(phone=query_phone)
                search_results += [format_response(contact.name, contact.phone, get_spam_likelihood(contact.phone)) for
                                   contact in contacts]
                if not contacts:
                    search_results.append(format_response(None, query_phone, get_spam_likelihood(query_phone)))

            #caching results for 5 min
            cache.set("name=" + query_phone,search_results,timeout=300)

        #paginating results
        page_number = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 5)
        return paginate_data(page_number,page_size,search_results)
