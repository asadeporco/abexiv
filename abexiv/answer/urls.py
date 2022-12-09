from django.urls import re_path
from answer.views import AnswerCreateListView, AnswerDetailView, AnswerListByUser

urlpatterns = [
     re_path('^question/(?P<question_id>[0-9]+)/$', AnswerCreateListView.as_view()),
     re_path('^(?P<answer_id>[0-9]+)/$', AnswerDetailView.as_view()),
     re_path('^user/(?P<user_id>[0-9]+)/$', AnswerListByUser.as_view()),
]
