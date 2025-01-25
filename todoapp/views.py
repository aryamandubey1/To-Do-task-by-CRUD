from token import tok_name
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Ensure the user is logged in

    if request.method == "POST":
        task = request.POST.get('task')
        if task:
            new_todo = todo(user=request.user, todo_name=task)
            new_todo.save()

    todos = todo.objects.filter(user=request.user)
    print(todos)
    context = {
        'todos': todos
    }
    return render(request, "todoapps/todo.html", context)
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('uname')
        number = request.POST.get('unumber')
        password = request.POST.get('upassword')

        validate_user = authenticate(username=username,password=password,number=number)
        if validate_user is not None:
            login(request, validate_user) # errror--------------------------------------------------l;
            return redirect('home')
        else:
            messages.error(request,'Error, wrong user detail or user does not exist')
            return redirect('login')
    return render(request,"todoapps/login.html")
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(password) < 3:
            messages.error(request,'Password must be at 3 character')
            return redirect('register')
        
        get_all_user_by_username = User.objects.filter(username=username)
        if get_all_user_by_username:
            messages.error(request,'Error,username already exist,using another')
            return redirect('register')
        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.save()

        messages.success(request,'User succesfully created login now ')
        return redirect('login')
    return render(request,"todoapps/register.html")


@login_required
def deleteTask(request,name):
    get_todo = todo.objects.get(user=request.user,todo_name=name)
    get_todo.delete()
    return redirect('home')

@login_required
def Update(request,name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = True
    get_todo.save()
    return redirect('home')


@login_required
def UNDO(request,name):
    get_todo = todo.objects.get(user=request.user, todo_name=name)
    get_todo.status = not get_todo.status
    get_todo.save()
    return redirect('home')

def Logoutview(request):
    logout(request)
    return redirect('login')



