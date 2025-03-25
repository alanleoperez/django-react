from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from rest_framework import viewsets

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
