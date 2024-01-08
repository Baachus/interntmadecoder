'''This is the views.py file for the todo app. This file is used to render the html file for the todo app.'''''
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .forms import TaskForm

tasks = [
    {"id": 1, "name": "Make video", "description": "Record your video with new camera", "priority": 1},
    {"id": 2, "name": "Edit video", "description": "Edit your video and make it smooth", "priority": 2},
    {"id": 3, "name": "Publish video", "description": "Publish your video to social media sites", "priority": 3}
    ]

def get_task_by_id(task_id):
    ''''This function is used to get the task by id.'''
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def index(request):
    ''''This function is used to render the html file for the todo app.'''
    taskform = TaskForm()
    if not 'tasks' in request.session:
        request.session['tasks'] = []
    ctx = {'tasks': request.session['tasks'], "form": taskform}
    return render(request, "todo/pages/index.html", ctx)

def add_task(request):
    ''''This function is used to add a task to the todo app.'''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = {
                "id": len(request.session['tasks']) + 1,
                "name": form.cleaned_data["task"],
                "description": form.cleaned_data["description"],
                "priority": form.cleaned_data["priority"]
            }
            request.session['tasks'].append(task)
            request.session.save()
            print(request.session['tasks'])
        else:
            return HttpResponse("Invalid form")
    return HttpResponseRedirect(reverse('todo:index'))

def task(request, id):
    ''''This function is used to render the html file for the todo app.'''
    ctx = {"task": get_task_by_id(id),}
    return render(request, 'todo/pages/task.html', ctx)

class AboutView(View):
    ''''This function is used to render the html file for the about with a class.'''

    def get(self, request):
        '''This function is used to render the html file for the about with a class.'''
        return HttpResponse("<h1>About page view</h1>")
