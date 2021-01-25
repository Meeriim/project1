from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo


def togo (request):
    return render (request, "index.html")


def second(request):
    return HttpResponse("My pages")


def testing (request):
    todo_list =ToDo.objects.all()
    return render (request, "html.html", {"todo_list": todo_list})


def add_todo (request):
    form = request.POST
    text = form["todo_text"]
    todo =ToDo(text=text)
    todo.save()
    return redirect(testing)
 

def delete_todo(request, id ):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(testing)
 

def mark_todo(request, id):
    todo =ToDo.objects.get(id=id)
    todo.is_fovorite = True 
    todo.save()
    return redirect(testing)
