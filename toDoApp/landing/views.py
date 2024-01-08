'''This is the views.py file for the landing app. This file is used to render the html file for the landing app.'''''
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

def index(request):
    ''''This function is used to render the html file for the landing app.'''
    return render(request, "landing/pages/landing_page.html")
