from django.urls import path, re_path
from user.views import UserCreateListView, UserRetrieveUpdateView

urlpatterns = [
    path('', UserCreateListView.as_view()),
    re_path('^(?P<user_id>[0-9]+)/$', UserRetrieveUpdateView.as_view()),
]
