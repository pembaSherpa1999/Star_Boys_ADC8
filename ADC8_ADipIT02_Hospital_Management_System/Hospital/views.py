#please before running this file install Pillow  for using image fields

from django.shortcuts import render, redirect
from .models import *
from django.template import Template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here for homepage.
def view_home(request):
    return render(request, 'index.html')


# creating view function for searching data form list
def view_search_page(request):
    #check whether the request is post or not
    if request.method == "POST":
        #get data from html file and assign to 'query'
        query = request.POST['search']
        #check whether there is input data in index
        if query:
            #compare the input query with data stored in patient.patentName 
            identical = patient.objects.filter(patientName__icontains = query)
            #check whether similer with patientName
            #if query is similer
            if identical:
                return render(request, 'search/searchForm.html', {'querySet': identical})
            #if query is not similer 
            else:
                return render(request, 'search/searchform2.html')
        #if empty index is searched
        else:
           return render(request, 'search/searchform3.html')
    else:
        return render(request, 'search/searchForm.html')



#method to give path to upload page 
def view_upload(request):
    return render(request, 'image/upload.html') 

#method that contains logic to store all the input data from upload page 
def view_uploadImage(request):
    #print this message in console
    print("image is uploading ................")
    name= request.POST['name']
    pic = request.FILES['patient image']
    about=request.POST['about image']
    #assign all data to patientpic model 
    patient = patientPic(pictureName=name,profilePic = pic,aboutPic=about)
    #save the object or data to database
    patient.save()
    #after saving data the page is opened again
    return render(request, 'image/upload.html')

#method that show image and act as download page with help of html page
def view_showimage(request):
    #assign all objects of patientpic to patient
    patientPicture=patientPic.objects.all()
    return render(request, 'image/images.html', {'patient':patientPicture})

#method for signup or register staff in signup page
def view_register_staff(request):
    if request.method =="GET":
        return render(request,'registration/register.html')
    else:
        user=request.POST['input_username']
        email=request.POST['email']
        enteredPassword=request.POST['input_password']
        staff=request.POST['is_staff']
        #assign all the posted data to model and save it to the user model
        staff = User.objects.create_user(username=user,email=email,password=enteredPassword,is_staff=staff)
        staff.save()
        return render(request,'registration/register.html')

#method for login page
def view_login_staff(request):
    if request.method =="GET":
        return render (request,'registration/login.html')
    else:
        #assign the input data from html page to respective variable
        user=request.POST['input_username']
        password=request.POST['input_password']
        #check whether the username and password is correct or not 
        staff = authenticate(request,username=user,password=password)
        print(staff)
        #if input user name and password is correct than
        if staff is not None:
            login(request,staff)
            return render(request,"index.html")
        #if input username and password is incorrect
        else:
            return HttpResponse("Authentication Failed")  

#method for logout
def view_logout(request):
    return redirect(view_login_staff)

