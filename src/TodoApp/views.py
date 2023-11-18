from django.shortcuts import render , redirect
from .models import Todo
from .forms import TodoForm , CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

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


def update_task(request , pk):
    task = Todo.objects.get(id=pk)
    
    form = TodoForm(instance=task)
    
    if request.method == 'POST':
        form = TodoForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {
        'form' : form
    }
    return render(request , 'TodoApp/update_task.html' , context)


def delete_task(request , pk):
    item = Todo.objects.get(id=pk)
    context = {
        'item' : item
    }
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    return render(request , 'TodoApp/delete.html' , context)


def register_user(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request , user + ' has been registered successfully!')

            return redirect('login')
        
    context = {'form':form}
    return render(request , 'TodoApp/register.html' , context)

def login_user(request):
    form = CreateUserForm(request.POST)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(request , username=username , password=password)
        
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            messages.info(request , 'Credentials are incorrect!')

        
    context = {'form':form}
    return render(request , 'TodoApp/login.html' , context)