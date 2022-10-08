from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from question.models import Question
from question.serializers import QuestionSerializer


class QuestionCreateListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['$description', '$title']

    def post(self, request, *args, **kwargs):
        question = Question(**request.data)
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

        

        
        