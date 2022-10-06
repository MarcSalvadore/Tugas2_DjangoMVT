import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django import forms

from django.contrib.auth.forms import UserCreationForm
from todolist.models import toDo
from django.contrib import messages
from todolist.forms import NewList
from django.http import HttpRequest
from django.http import HttpResponseRedirect

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_list(request: HttpRequest):
    # data_kegiatan = ToDo.objects.filter(user=request.user).all()
    user = request.user
    data_kegiatan = toDo.objects.all()
    context = {
    'list_kegiatan': data_kegiatan,
    'nama': user.username,
    'last_login': request.COOKIES['last_login'],
    }  
    return render(request, "todolist.html", context)

def register(request: HttpRequest):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created!")
            return redirect("todolist:login")
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_list"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Incorrect Username or Password!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request: HttpRequest):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request: HttpRequest):
    if request.method == "POST":
        form = NewList(request.POST)
        if form.is_valid():
            task = toDo(
                date=str(datetime.datetime.now().date()),
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                user=request.user,
            )
            task.save()
            messages.success(request, "Saved success!")
            return redirect("todolist:show_list")

    form = NewList()
    context = {"form": form}
    return render(request, "newtask.html", context)

def delete_task(request: HttpRequest, post_id:int):
    if request.method == "POST":
        task = toDo.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.delete()
            messages.success(request, "Task has been deleted!")
        else:
            messages.error(request, "Task not found!")
    return redirect("todolist:show_list")

def update_task(request: HttpRequest, post_id:int):
    if request.method == "POST":
        task = toDo.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.is_finished = not task.is_finished
            task.save()
            messages.success(request, "Update success!")
        else:
            messages.error(request, "Task not found!")
    return redirect("todolist:show_list")
    