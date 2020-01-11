from django.shortcuts import render
from .models import *
# Create your views here.

def uploadImage(request):
    return render(request, 'upload.html')

def upload(request):
    print("image uploading .. .. .. . .")
    picture  = print(request.FILES['patient image'])
    photo = patient(profile = picture)
    photo.save()
    return render(request, 'upload.html')