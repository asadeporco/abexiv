from django.urls import path
from answer.views import AnswerCreateListView

urlpatterns = [
    path('', AnswerCreateListView.as_view()),
]
