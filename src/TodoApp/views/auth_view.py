from django.shortcuts import render , redirect
from forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:    
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
    
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
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

def logout_user(request):
    logout(request)
    return redirect('login')