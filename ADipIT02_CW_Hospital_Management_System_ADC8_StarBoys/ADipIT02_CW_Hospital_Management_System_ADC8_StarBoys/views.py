from django.http import HttpResponse
from django.shortcuts import render

def hello_world_view(request):
    return HttpResponse("Hello world this is herald college")
