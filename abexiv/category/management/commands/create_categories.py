import email
from email.policy import default
from django.core.management.base import BaseCommand
from django.utils import timezone
from category.enums import Category
from user.models import User


default_categories = [
        "math",
        "history",
        "science",
        "general",
    ]

class Command(BaseCommand):
    help = 'Create default categories'
    
    

    def handle(self, *args, **kwargs):
        for category in default_categories:
            Category.objects.create(name=category)
        