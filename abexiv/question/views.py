from email.policy import default
from unicodedata import category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from question.models import Question
from question.serializers import QuestionSerializer
from utils.custom_pagination import CustomPagination



class QuestionCreateListView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    filter_backends = [SearchFilter]
    search_fields = ['$description', '$title']
    
    def get_queryset(self):
        categories = self.request.GET.getlist("category")
        return Question.objects.select_related("category").filter(category_id__in=categories)

    def post(self, request, *args, **kwargs):
        request_params = request.data
        
        question = Question()
        question.title = request_params.get("title")
        question.description = request_params.get("description")
        question.category_id = request_params.get("category_id")
        
        question.user = request.user
        question.save()
        return Response(QuestionSerializer(question).data)

class QuestionDetailRetrieve(generics.RetrieveUpdateAPIView):
    serializer_class = QuestionSerializer

    def get(self, request, question_id, *args, **kwargs):            
        question = Question.objects.filter(id=question_id).first()
        if not question:
            return Response({
                "message": f"Question with id {question_id} does not exist"
            })
        
        data = QuestionSerializer(question).data

        return Response(data)

    def update(self, request, question_id, *args, **kwargs):
        question = Question.objects.filter(id=question_id).first()
        if not question:
            return Response({
                "message": f"Question with id {question_id} does not exist"
            })
        
        params = request.data

        question.title = params.get("title")
        question.description = params.get("description")
        question.save()

        data = QuestionSerializer(question).data
        return Response(data)

        

        
        