from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

import logging
import os

from .serializers import RegisterSerializer, LoginSerializer

class Register(APIView):
    """
    This view allows new users to register by providing the required details.
    It validates the data using the `RegisterSerializer` and creates a new user.
    """
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=201)
        return Response(serializer.errors, status=400)



class Login(APIView):
    """
     This view authenticates a user using their phone number and password.
    Upon successful authentication, it generates and returns a JWT access and refresh token.
    """
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']

            #authenticate
            user = authenticate(username=phone, password=password)

            if user is not None:
                # If authentication is successful, generate JWT token
                refresh = RefreshToken.for_user(user)
                return Response({
                    'message': 'Login successful!',
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh)
                }, status=200)
            else:
                return Response({
                    'error': 'Invalid phone number or password.'
                }, status=401)
        return Response(serializer.errors, status=400)


