from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer


class UserCreateListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer