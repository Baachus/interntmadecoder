'''This is the urls.py file for the todo app. This file is used to create the url for the todo app.'''
from django.urls import include, path
from .views import index

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
]
