'''This is the views.py file for the todo app. This file is used to render the html file for the todo app.'''''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .forms import TaskForm
from .models import TaskModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import json

def login_user(request):
    ''''This function is used to render the html file for the todo app.'''
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('todo:index'))
    return render(request, "todo/pages/login.html")

@login_required(login_url='todo:login')
def logout_user(request):
    ''''This function is used to render the html file for the todo app.'''
    logout(request)
    return HttpResponseRedirect(reverse('todo:login'))

@login_required(login_url='todo:login')
def index(request):
    ''''This function is used to render the html file for the todo app.'''
    taskform = TaskForm()
    tasks = TaskModel.objects.filter(user=request.user)
    ctx = {'tasks': tasks, "form": taskform, "user": request.user}
    return render(request, "todo/pages/index.html", ctx)

def delete_task(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        task_id = body['taskId']
        task = TaskModel.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect(reverse('todo:index'))
    
    return HttpResponseRedirect(reverse('todo:index'))

def register_user(request):
    ''''This function is used to render the html file for the todo app.'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get("username")
            password = request.POST.get("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('todo:index'))
    return render(request, "todo/pages/register.html")

def add_task(request):
    ''''This function is used to add a task to the todo app.'''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = TaskModel(
                user=request.user,
                name=form.cleaned_data["task"],
                description=form.cleaned_data["description"],
                priority=form.cleaned_data["priority"]
            )
            task.save()
        else:
            return HttpResponse("Invalid form")
    return HttpResponseRedirect(reverse('todo:index'))

def task(request, id):
    ''''This function is used to render the html file for the todo app.'''
    task = TaskModel.objects.get(id=id)
    ctx = {"task": task}
    return render(request, 'todo/pages/task.html', ctx)

class AboutView(View):
    ''''This function is used to render the html file for the about with a class.'''

    def get(self, request):
        '''This function is used to render the html file for the about with a class.'''
        return HttpResponse("<h1>About page view</h1>")
