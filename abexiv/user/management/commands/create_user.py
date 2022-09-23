import email
from django.core.management.base import BaseCommand
from django.utils import timezone
from user.models import User


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        user = User.objects.filter(username="admin")
        if user:
            return
        user = User(username="admin",
                    is_superuser=True,
                    email="admin@admin.com",
                    first_name="admin",
                    last_name="admin",
                    is_staff=True,
                    is_active=True)
        user.set_password("admin")
        user.save()
        