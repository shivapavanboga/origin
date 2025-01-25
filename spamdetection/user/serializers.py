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
        return User.objects.create_user(
            username=validated_data['phone'],  # Using phone as username
            password=validated_data['password'], #this field will be hashed
            name=validated_data['name'],
            phone=validated_data['phone'],
            email=validated_data.get('email')
        )

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True)
    def validate_phone(self,phone):
        if not validate_phone_number(phone):
            raise serializers.ValidationError(
                "Invalid phone number format."
            )
        return phone

