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

# Create your views here for homepage.
def view_home(request):
    return render(request, 'index.html')

#view function for adding patient detail
def view_patient(request):
    return render(request, 'patient.html')

#view function with main adding method to add patient detail
def view_patientdata_save(request):
    if request.method == "POST":
        get_all = request.POST#here post method get all the data which is posted in html page or form
        print(get_all)#method to show key value and all posted value in terminal or comand prom
        get_PatientName = request.POST['patient_PatientName']#here post method get the data which is posted in html page or form
        get_PatientAddress = request.POST['patient_Patientaddress']
        get_PatientPhoneNo = request.POST['patient_PatientphoneNo']
        get_PatientAge= request.POST['patient_Patientage']
        get_PatientSex = request.POST['patient_Patientsex']
        patient_obj = patient(patientName=get_PatientName,patientAddress=get_PatientAddress,patientPhoneNo=get_PatientPhoneNo,patientAge =get_PatientAge,patientSex=get_PatientSex )
        patient_obj.save()
        return render(request,'patient.html')
        
    else:
        return HttpResponse("Error in saving")

#view function to go to show  patient list 
def view_patient_page(request):
    return render(request,'patient.html')

def view_patient_lists(request):
    list_of_patient=patient.objects.all()
    print(list_of_patient)
    context_variable = {
        'patients':list_of_patient
    }
    return render(request,'patientview.html',context_variable)
     

# Functionality of adding doctor information
def view_add_doctor_detail(request):
    return render(request, 'doctorDetail.html')

def view_doctordata_save(request):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_Name = request.POST['doctor_DoctorName']
        get_Address = request.POST['doctor_DoctorAddress']
        get_Contact = request.POST['doctor_DoctorContact']
        get_department = request.POST['doctor_DoctorDepartment']
        get_education = request.POST['doctor_DoctorEducation']
        doctor_obj = doctor(Name=get_Name,Address=get_Address,Contact=get_Contact,department=get_department,education=get_education)
        doctor_obj.save()
        return redirect(view_add_doctor_detail)
    else:
        return HttpResponse("error occured")

# Functionality of viewing doctor information

def view_doctor_page(request):
    return render(request,'doctorDetail.html')

def view_doctor_lists(request):
    list_of_doctor=doctor.objects.all()
    print(list_of_doctor)
    context_variable = {
        'doctors':list_of_doctor
    }
    return render(request,'doctorview.html',context_variable)

# for deleting info:
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

# for updating patient info:
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



# creating view function for searching data form list
def view_search_page(request):
    if request.method == "POST":
        query = request.POST['srh']
        if query:
            identical = patient.objects.filter(patientName__icontains = query)
            if identical:
                return render(request, 'search/searchForm.html', {'querySet': identical})
            else:
                return render(request, 'search/searchform2.html')
        else:
           return render(request, 'search/searchform3.html')
    else:
        return render(request, 'search/searchForm.html')


def get_data_queryset(query=None):
    if request.method == "POST":
        qs = patient.objects.all()
        patient_name= request.POST['patient_PatientName']
        patient_address= request.POST['patient_Patientaddress']
        if patient_name != '' and patient_address is not None:
            qs = qs.filter(patient_PatientName__icontains=patient_name)
            Context = {
                'querySet': qs
                }
            return render(request ,'form.html',Context)
    else:
        return HttpResponse("error occured")

# Functionality of creating appointment details

def view_appointment_details(request):
    return render(request,'appointmentDetails.html')


def view_appointment_save(request):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_patientName = request.POST['patientName']
        get_doctorName = request.POST['doctorName']
        get_Date = request.POST['Date']
        get_Time = request.POST['Time']
        appointment_obj = Appointment(patientName=get_patientName,doctorName=get_doctorName,Date=get_Date,Time=get_Time)
        appointment_obj.save()
        return HttpResponse("Save record")
    else:
        return HttpResponse("error occured")

# Functionality of viewing appointment details
# 
def view_appointment_page(request):
    return render(request,'appointmentDetail.html')

def view_appointment_lists(request):
    list_of_Appointment=Appointment.objects.all()
    print(list_of_Appointment)
    context_variable = {
        'appointments':list_of_Appointment
    }
    return render(request,'appointmentview.html',context_variable)
     

# Functionality of creating bills details
# 
def view_billing_details(request):
    return render(request,'Billing.html')


def view_billdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_BillNo = request.POST['BillNO']
        get_PatientName = request.POST['PatientName']
        get_Amount = request.POST['Amount']
        bill_obj = Bill(BillNo=get_BillNo,PatientName=get_PatientName,Amount=get_Amount)
        bill_obj.save()
        return HttpResponse("save record in database")
    else:
        return HttpResponse("error occured")

# Functionality of viewing bills details

def view_bill_page(request):
    return render(request,'Billing.html')

def view_bill_lists(request):
    list_of_bill=Bill.objects.all()
    print(list_of_bill)
    context_variable = {
        'bills':list_of_bill
    }
    return render(request,'Billview.html',context_variable)
     


# Functionality of creating Testoperation details

def view_Testoperation_details(request):
    return render(request,'TestOperation.html')

def view_testdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_PatientID = request.POST['patientID']
        get_PatientName = request.POST['patientName']
        get_prescribeMedicine= request.POST[ 'patientPrescribeMedicine']
        get_prescribeTratment= request.POST[ 'patientPrescribeTreatment']
        get_report= request.POST['patientReport']
        TestOperation_obj = TestOperation (PatientID=get_PatientID,PatientName=get_PatientName,prescribeMedicine=get_prescribeMedicine,prescribeTratment=get_prescribeTratment,report=get_report)
        TestOperation_obj.save()
        return HttpResponse("save record in database")
    else:
        return HttpResponse("error occured")

# Functionality of viewing Testoperation details
# 
def view_test_page(request):
    return render(request,'TestOperation.html')

def view_test_lists(request):
    list_of_TestOperation=TestOperation.objects.all()
    print(list_of_TestOperation)
    context_variable = {
        'TestOperation':list_of_TestOperation
    }
    return render(request,'TestOperationview.html',context_variable)


@csrf_exempt # delection the csrf token detection method 
def view_upload(request):
    return render(request, 'upload.html')

@csrf_exempt # delection the csrf token detection method 
def view_uploadImage(request):
    print("image is uploading ................")
    name= request.POST['name']
    pic = request.FILES['patient image']
    about=request.POST['about image']
    patient = patientPic(pictureName=name,profilePic = pic,aboutPic=about)
    patient.save()
    return render(request, 'upload.html')

# Function for showing images
def view_showimage(request):
    patient1=patientPic.objects.all()
    return render(request, 'images.html', {'patient':patient1})


# Function for registration
def view_register_staff(request):
    if request.method =="GET":
        return render(request,'register.html')
    else:
        print(request.POST)
        staff = User.objects.create_user(username=request.POST['input_username'],email=request.POST['email'],password=request.POST['input_password'],is_staff=request.POST['is_staff'])
        staff.save()
        return render(request,'register.html')
# Function for Login
def view_login_staff(request):
    print(request.POST)
    if request.method =="GET":
        return render (request,'login.html')
    else:
        print(request.POST)
        staff = authenticate(request,username=request.POST['input_username'],password=request.POST['input_password'])
        print(staff)
        if staff is not None:
            login(request,staff)
            return render(request,"index.html")
        else:
            return HttpResponse("Authentication Failed")  

# Function for Logout

def view_logout(request):
    return redirect(view_login_staff)

