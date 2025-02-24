from rest_framework import serializers

from .models import User
from .utils import validate_phone_number


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'password', 'name', 'email']
    def validate_phone(self,phone):
        if not validate_phone_number(phone):
            raise serializers.ValidationError(
                "Invalid phone number format."
            )
        return phone

    def create(self, validated_data):
        """Create or update an unregistered user"""
        phone = validated_data['phone']
        password = validated_data['password']
        name = validated_data['name']
        email = validated_data.get('email')

        # Check if the user exists in the global database
        user, created = User.objects.get_or_create(phone=phone)
        if user.is_registered:
            raise serializers.ValidationError("User already exists")
        if not user.is_registered:
            user.name = name
            user.email = email
            user.is_registered = True  # Now marked as registered
            user.set_password(password)  # Ensure password is hashed
            user.save()
        return user

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True)
    def validate_phone(self,phone):
        if not validate_phone_number(phone):
            raise serializers.ValidationError(
                "Invalid phone number format."
            )
        return phone

