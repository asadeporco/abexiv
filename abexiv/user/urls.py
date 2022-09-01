from django.urls import path
from user.views import UserCreateListView

urlpatterns = [
    path('', UserCreateListView.as_view()),
]
