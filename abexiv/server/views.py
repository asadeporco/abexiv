from webbrowser import get
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

class Test(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        return Response({"test": "yes"})
