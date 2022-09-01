from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from question.models import Question
from question.serializers import QuestionSerializer


class QuestionCreateListView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        question = Question(**request.data)
        question.user = request.user
        question.save()
        return Response(QuestionSerializer(question).data)