from django.shortcuts import render
from user.services import UserService
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response


class UserCreateListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset =  User.objects.all()
        