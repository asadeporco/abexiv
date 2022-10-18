from rest_framework import serializers
from question.models import Question
from user.serializers import UserShortSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()
    class Meta:
        model = Question
        fields = [
            "created_at",
            "title",
            "description",
            "user",
        ]
