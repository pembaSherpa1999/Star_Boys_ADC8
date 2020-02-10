from django.shortcuts import render, redirect
from .models import *
from django.template import Template,Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.template import Context
from django.contrib.auth.models import User
from django.views.decorators.csrf import *
from django.contrib.auth import authenticate, login
import os
from django.conf import settings

# for deleting patients information!!!
#delete 
def view_patient_delete(request,ID):  
    print(ID)
    patient_obj = patient.objects.get(id=ID)  
    context_variable={
        'patient':patient_obj
    }
    patient_obj.delete()
    return render(request,'patientdelete.html',context_variable) 

def view_update(request, ID):
    return render(request,'patientupda.html')

# for updating patients information!!!
def view_patient_update(request, ID):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_PatientName = request.POST['patient_PatientName']
        get_PatientAddress = request.POST['patient_Patientaddress']
        get_PatientPhoneNo = request.POST['patient_PatientphoneNo']
        get_PatientAge= request.POST['patient_Patientage']
        get_PatientSex = request.POST['patient_Patientsex']
        patient_obj = patient(patientName=get_PatientName, patientAddress= get_PatientAddress,patientPhoneNo=get_PatientPhoneNo,
        patientAge =get_PatientAge,patientSex=get_PatientSex )
        patient_obj.save()
        return redirect(view_patient_lists)
    else:
        print(ID)
        patient_obj = patient.objects.get(id=ID)  
        context_variable={
            'patient':patient_obj
        }
        return render(request,"patientupdate.html",context_variable)