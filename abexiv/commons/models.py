from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey
from question.models import Question
from answer.models import Answer


class QuestionAnswer(models.Model):
    question = ForeignKey(Question, on_delete=SET_NULL, null=True)
    answer = ForeignKey(Answer, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f'{self.question} : {self.answer}'

