from django.urls import path, re_path
from question.views import QuestionCreateListView, QuestionDetailRetrieve

urlpatterns = [
    path('', QuestionCreateListView.as_view()),
    re_path('^(?P<question_id>[0-9]+)/$', QuestionDetailRetrieve.as_view()),
]