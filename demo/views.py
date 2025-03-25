from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import Book


def first(request):
    books = Book.objects.all()
    return render(request, "First_temp.html", {"books": books})
