from django.db import models

from user.models import User
from django.db.models.deletion import SET_NULL, CASCADE

from question.models import Question


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=CASCADE, null=False)

    def __str__(self):
        return self.title
