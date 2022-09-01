from django.urls import path
from question.views import QuestionCreateListView

urlpatterns = [
    path('', QuestionCreateListView.as_view()),
]