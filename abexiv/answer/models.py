from django.db import models

from user.models import User
from django.db.models.deletion import SET_NULL


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
