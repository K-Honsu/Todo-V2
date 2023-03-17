from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "first_name", "last_name", "email", "password"]



# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','first_name', 'last_name', 'email', 'password']