from rest_framework import serializers
from user.utils import validate_phone_number
from .models import SpamReport

class SpamSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15)
    class Meta:
        model=SpamReport
        fields = ['phone']
    def validate_phone(self, phone):
        if not validate_phone_number(phone):
            raise serializers.ValidationError(
                "Invalid phone number format."
            )
        return phone
