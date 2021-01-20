from django.shortcuts import render, HttpResponse


def togo (request):
    return render (request, "ilgiz.html")


def second(request):
    return HttpResponse("My pages")