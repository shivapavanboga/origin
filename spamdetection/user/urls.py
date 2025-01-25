from django.urls import path
from .views import Register, Login

urlpatterns = [
    path('register/', Register.as_view(), name='register'),  # User registration
    path('login/', Login.as_view(), name='login'),
    ]