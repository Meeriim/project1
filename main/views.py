from django.shortcuts import render, HttpResponse


def togo (request):
    return render (request, "index.html")


def second(request):
    return HttpResponse("My pages")