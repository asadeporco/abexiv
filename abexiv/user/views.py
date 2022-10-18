from django.shortcuts import render
from user.services import UserService
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics
from user.models import User
from user.serializers import UserSerializer
from rest_framework.response import Response

from rest_framework.filters import SearchFilter

from utils.custom_pagination import CustomPagination



class UserCreateListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['$username', '$first_name', '$last_name']

    queryset =  User.objects.all()


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    
    def __init__(self, **kwargs):
        self.service = UserService()
   
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
        
        data = self.service.insert(user, request_params)

        

        data = UserSerializer(data).data

        return Response(data)