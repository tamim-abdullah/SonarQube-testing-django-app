from django.shortcuts import render
from .models import Todo

def index(request):
    tasks = Todo.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request , 'TodoApp/list.html' , context)
