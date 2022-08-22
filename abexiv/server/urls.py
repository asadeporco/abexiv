from django.contrib import admin
from django.urls import path
from server.views import Test

urlpatterns = [
    path('test/', Test.as_view()),
]
