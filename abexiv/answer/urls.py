from django.urls import re_path
from answer.views import AnswerCreateListView, AnswerDetailView

urlpatterns = [
     re_path('^question/(?P<question_id>[0-9]+)/$', AnswerCreateListView.as_view()),
     re_path('^(?P<answer_id>[0-9]+)/$', AnswerDetailView.as_view()),
]
