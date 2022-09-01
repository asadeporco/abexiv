from rest_framework import generics

from question.models import Question
from question.serializers import QuestionSerializer


class QuestionCreateListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
