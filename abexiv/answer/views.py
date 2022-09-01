from rest_framework import generics

from answer.models import Answer
from answer.serializers import AnswerSerializer
from answer.service import AnswerService


class AnswerCreateListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def post(self, request, *args, **kwargs):
       pass
