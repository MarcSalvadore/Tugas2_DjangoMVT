from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from django.core import serializers
from django.urls import reverse
from django import forms

from datetime import date
import datetime

from todolist.models import toDo
from todolist.forms import NewList

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_list(request: HttpRequest):
    # data_kegiatan = ToDo.objects.filter(user=request.user).all()
    user = request.user
    data_kegiatan = toDo.objects.filter(user=request.user)
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
            messages.success(request, "Create Account Success!")
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

@login_required(login_url='/todolist/login/')
def logout_user(request: HttpRequest):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
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

@login_required(login_url='/todolist/login/')
def delete_task(request: HttpRequest, post_id:int):
    if request.method == "POST":
        task = toDo.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.delete()
            messages.success(request, "Task has been deleted!")
        else:
            messages.error(request, "Task not found!")
    return redirect("todolist:show_list")

@login_required(login_url='/todolist/login/')
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

@login_required(login_url='/todolist/login/')
def show_list_json(request: HttpRequest):
    task = toDo.objects.filter(user=request.user).order_by("date").all()
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

@login_required(login_url='/todolist/login/')
def add_task_json(request: HttpRequest):
    if request.method == "POST":
        task = toDo(
            user = request.user,
            date = date.fromisoformat(request.POST["date"]),
            title = request.POST["title"],
            description = request.POST["description"],
        )
        task.save
        return HttpResponse(
            serializers.serialize("json", [task]),
            content_type = "application/json",
            )
    return HttpResponse("Invalid method", status_code=405)

@login_required(login_url='/todolist/login/')
def delete_task_json(request: HttpRequest, post_id: int):
    if request.method == "DELETE":
        task = toDo.objects.filter(id=post_id, user=request.user).first()
        if task:
            task.delete()
            return HttpResponse("OK")
        else:
            return HttpResponse("Not Found", status_code=404)
    return HttpResponse("Invalid method", status_code=405)
    