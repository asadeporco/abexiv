from django.shortcuts import render
from user.services import UserService
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter



class UserCreateListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['$username', '$first_name', '$last_name']

    queryset =  User.objects.all()


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
   
    def get(self, request, user_id, *args, **kwargs):
        user = User.objects.filter(id=user_id).first()

        if not user:
            return Response({
                "message": f"User with id {user_id} does not exist"
            })
        data = UserSerializer(user).data

        return Response(data)
    
    
    def update(self, request, user_id, *args, **kwargs):
        user = User.objects.filter(id=user_id).first()

        if not user:
            return Response({
                "message": f"User with id {user_id} does not exist"
            })

        request_params = request.data
        user.username = request_params.get('')

        user.username = request_params.get("username")
        user.first_name = request_params.get("first_name")
        user.last_name = request_params.get("last_name")
        user.save()

        data = UserSerializer(user).data

        return Response(data)