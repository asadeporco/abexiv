from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter
from category.models import Category
from category.serializers import CategorySerializer

from utils.custom_pagination import CustomPagination



class CategoryCreateListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['$name']
    
    def get_queryset(self):
        return Category.objects.all()

    def post(self, request, *args, **kwargs):
        request_params = request.data
        
        category = Category()
        category.name = request_params.get("name")

        category.save()

        return Response(CategorySerializer(category).data)
