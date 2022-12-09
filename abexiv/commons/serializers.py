from rest_framework import serializers
from answer.serializers import AnswerSerializer
from question.serializers import QuestionSerializer
from answer.models import Answer


class UserAnswaresWithQiestions(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = [
                    "created_at",
                    "description",
                    "user",
                    'question'
                  ]
