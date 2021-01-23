from django.shortcuts import render, HttpResponse
from .models import ToDo


def togo (request):
    return render (request, "index.html")


def second(request):
    return HttpResponse("My pages")


def testing (request):
    todo_list =ToDo.objects.all()
    return render (request, "html.html", {"todo_list": todo_list})