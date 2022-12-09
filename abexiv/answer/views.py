from urllib import response
from rest_framework import generics

from answer.models import Answer
from answer.serializers import AnswerSerializer

from question.models import Question

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from answer.service import AnswerService
from utils.custom_pagination import CustomPagination
from commons.serializers import UserAnswaresWithQiestions

class AnswerCreateListView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

    def __init__(self):
        self.service = AnswerService()

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        return Answer.objects.select_related("user").filter(question_id=question_id)


    def post(self, request, question_id, *args, **kwargs):

        question = Question.objects.filter(id=question_id).first()

        if not question:
            return Response({
                "message": f"Question with id {question_id} does not exist"
            })

        request_data = request.data

        data = self.service.create_answer(question_id, request_data, request.user)

        answer = AnswerSerializer(data).data

        return Response(answer)
        

class AnswerDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = AnswerSerializer

    def __init__(self):
        self.service = AnswerService()


    def get(self, request, answer_id, *args, **kwargs):
        answer = Answer.objects.filter(id=answer_id).first()

        if not answer:
            return Response({
                "message": f"Answer with id {answer_id} does not exist"
            })

        data = AnswerSerializer(answer).data

        return Response(data)

    
    def update(self, request, answer_id, *args, **kwargs):
        answer = Answer.objects.filter(id=answer_id).first()

        if not answer:
            return Response({
                "message": f"Answer with id {answer_id} does not exist"
            })
        request_params = request.data

        answer.title = self.service.update_answer(answer_id, request_params)

        data = AnswerSerializer(answer).data

        return Response(data)


class AnswerListByUser(generics.ListAPIView):
    serializer_class = UserAnswaresWithQiestions
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination

     
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")

        return Answer.objects.select_related("question").filter(user_id=user_id)
