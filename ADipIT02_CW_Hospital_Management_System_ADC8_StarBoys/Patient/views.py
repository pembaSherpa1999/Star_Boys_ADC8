from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,context
from .views import *

# Create your views here.
def view_hello_world(request):
    return HttpResponse("Hello world")

def view_hello_world_template(request):
    return render(request,'patient/new.html')
