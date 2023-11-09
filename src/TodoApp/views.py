from django.shortcuts import render , redirect
from .models import Todo
from .forms import TodoForm

def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()     
        return redirect('/')
            
    
    context = {
        'tasks' : tasks,
        'form' : form
    }
    return render(request , 'TodoApp/list.html' , context)
