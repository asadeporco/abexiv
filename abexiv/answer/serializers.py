from rest_framework import serializers
from answer.models import Answer
from user.serializers import UserShortSerializer


class AnswerSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()
    class Meta:
        model = Answer
        fields = [
                    "created_at",
                    "title",
                    "description",
                    "user",
                  ]
