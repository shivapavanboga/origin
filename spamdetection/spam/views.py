from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import SpamReport
from .serializers import SpamSerializer


class MarkSpam(APIView):
    """
    API to mark a phone number as spam.
    Ensures authenticated access and prevents duplicate spam reports by the same user.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        # Deserialize and validate incoming data
        serializer = SpamSerializer(data=request.data)

        # Check if the provided data is valid
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            print(phone,request.user)
            report, created = SpamReport.objects.get_or_create(
                phone=phone,
                spammed_by=request.user
            )

            # If the report already exists, inform the user
            if not created:
                return Response(
                    {"message": "This number has already been marked as spam by you."},
                    status=400
                )

            # If successfully created, return a success message
            return Response(
                {"message": "Number marked as spam successfully."},
                status=201
            )

        # If the data is invalid, return validation errors
        return Response(serializer.errors, status=400)
