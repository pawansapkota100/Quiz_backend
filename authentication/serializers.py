
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser
user=get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True, required=True)

    class Meta:
        model = user
        fields = ('email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
        
