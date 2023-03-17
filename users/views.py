from .serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
User = get_user_model()


class RegisterUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer