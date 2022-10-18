from django.urls import path, re_path
from category.views import CategoryCreateListView

urlpatterns = [
    path('', CategoryCreateListView.as_view()),
]
