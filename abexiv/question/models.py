from unicodedata import category
from django.db import models
from category.models import Category

from user.models import User
from django.db.models.deletion import SET_NULL

class Question(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
