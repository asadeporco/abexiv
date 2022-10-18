from rest_framework import serializers
from category.serializers import CategorySerializer
from question.models import Question
from user.serializers import UserShortSerializer


class QuestionSerializer(serializers.ModelSerializer):
    user = UserShortSerializer()
    category = CategorySerializer()
    class Meta:
        model = Question
        fields = [
            "id",
            "created_at",
            "title",
            "description",
            "user",
            "category"
        ]
