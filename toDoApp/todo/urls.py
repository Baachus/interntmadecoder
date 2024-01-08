'''This is the urls.py file for the todo app. This file is used to create the url for the todo app.'''
from django.urls import path
from .views import AboutView, index, task, add_task

app_name = 'todo'

urlpatterns = [
    path('', index, name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('task/<int:id>', task, name='task'),
    path('add_task/', add_task, name='add_task')
]
