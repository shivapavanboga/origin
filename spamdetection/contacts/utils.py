from django.core.paginator import Paginator
from rest_framework.response import Response
from .models import Contact
def paginate_data(page_number,page_size,data):
    paginator = Paginator(data, page_size)
    try:
        page = paginator.page(page_number)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    return Response({
        "count": paginator.count,
        "total_pages": paginator.num_pages,
        "current_page": page_number,
        "results": page.object_list,  # The paginated data
        "next": page.has_next(),
        "previous": page.has_previous(),
    },status=200)

def format_response(name, phone, likelihood, email=None):
    return {
        "name": name,
        "phone": phone,
        "spam_likelihood": likelihood,
        "email": email,
    }

def get_email_if_contact_exists(user, logged_in_user_phone):
    return user.email if Contact.objects.filter(user=user, phone=logged_in_user_phone).exists() else None
