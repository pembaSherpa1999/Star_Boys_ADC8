#please before running this file install Pillow  for using image fields

from django.shortcuts import render, redirect
from .models import *
from django.template import Template,Context
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.template import Context
from django.contrib.auth.models import User
from django.views.decorators.csrf import *
from django.contrib.auth import authenticate, login
from django.conf import settings

# Create your views here for homepage.
def view_home(request):
    return render(request, 'index.html')

#view function for adding patient detail
def view_patient(request):
        return render(request, 'Patient/patient.html')
    

#view function with main adding method to add patient detail
def view_patientdata_save(request):
    if request.method == "POST":
        #here post method get all the data which is posted in html page or form
        get_all = request.POST
        #method to show key value and all posted value in terminal or comand prom
        print(get_all)
        #here post method get the data which is posted in html page or form
        get_PatientName = request.POST['patient_PatientName']
        get_PatientAddress = request.POST['patient_Patientaddress']
        get_PatientPhoneNo = request.POST['patient_PatientphoneNo']
        get_PatientAge= request.POST['patient_Patientage']
        get_PatientSex = request.POST['patient_Patientsex']
        #assign and save data from index to database
        patient_obj = patient(patientName=get_PatientName,patientAddress=get_PatientAddress,patientPhoneNo=get_PatientPhoneNo,patientAge =get_PatientAge,patientSex=get_PatientSex )
        patient_obj.save()
        return render(request,'Patient/patient.html')
    else:
        return HttpResponse("Error in saving")

#view function for path to show  patient list 
def view_patient_page(request):
    return render(request,'Patient/patient.html')

#view function main logic to show  patient list
def view_patient_lists(request):
    list_of_patient=patient.objects.all()
    print(list_of_patient)
    context_variable = {
        'patients':list_of_patient
    }
    return render(request,'Patient/patientview.html',context_variable)
     
#function to add doctor detail
def view_add_doctor_detail(request):
    return render(request, 'Doctor/doctorDetail.html')

#function to add doctor detail logic
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

#view function to show doctor list
def view_doctor_page(request):
    return render(request,'Doctor/doctorDetail.html')

#view function that saves doctor detail to database
def view_doctor_lists(request):
    list_of_doctor=doctor.objects.all()
    print(list_of_doctor)
    context_variable = {
        'doctors':list_of_doctor
    }
    return render(request,'Doctor/doctorview.html',context_variable)

# # for deleting info:
#delete 
def view_patient_delete(request,ID):  
    print(ID)
    patient_obj = patient.objects.get(id=ID)  
    context_variable={
        'patient':patient_obj
    }
    patient_obj.delete()
    return render(request,'Patient/patientdelete.html',context_variable) 

def view_update_data(request, ID):
    return render(request,'Patient/updatePatient.html')

# for updating patient info:
def view_patient_update(request,ID):
    if request.method == "post":
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
        return render(request,"Patient/updatePatient.html",context_variable) 



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

#view function to which act as path for assing appointent detail
def view_appointment_details(request):
    return render(request,'appointment/appointmentDetails.html')

#view function having main saving logic
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
        return redirect(view_appointment_details)
    else:
        return HttpResponse("error occured")

#view function to show appointment detail
def view_appointment_page(request):
    return render(request,'appointment/appointmentDetail.html')

#view function for logic of showing appointment detail
def view_appointment_lists(request):
    list_of_Appointment=Appointment.objects.all()
    print(list_of_Appointment)
    context_variable = {
        'appointments':list_of_Appointment
    }
    return render(request,'appointment/appointmentview.html',context_variable)
     


#view function to add billing detail
def view_billing_details(request):
    return render(request,'Billing/Billing.html')


#view function with logic to add billing detai
def view_billdata_save(request):
    if request.method == "POST":
        get_all = request.POST
        print(get_all)
        get_BillNo = request.POST['BillNO']
        get_PatientName = request.POST['PatientName']
        get_Amount = request.POST['Amount']
        bill_obj = Bill(BillNo=get_BillNo,PatientName=get_PatientName,Amount=get_Amount)
        bill_obj.save()
        return render(request,'Billing/Billing.html')
    else:
        return HttpResponse("error occured")

#view function to show billing detail
def view_bill_page(request):
    return render(request,'Billing/Billing.html')

#view function having logic to show bill detail
def view_bill_lists(request):
    list_of_bill=Bill.objects.all()
    print(list_of_bill)
    context_variable = {
        'bills':list_of_bill
    }
    return render(request,'Billing/Billview.html',context_variable)
     
#view function to add test operation  detail
def view_Testoperation_details(request):
    return render(request,'Test&Operation/TestOperation.html')

#view function with logic to add test operation detai
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
        return render(request,'Test&Operation/TestOperation.html')
    else:
        return HttpResponse("error occured")

#view function to show test operation detail
def view_test_page(request):
    return render(request,'Test&Operation/TestOperation.html')


#view function having logic to show test operation  detail
def view_test_lists(request):
    list_of_TestOperation=TestOperation.objects.all()
    print(list_of_TestOperation)
    context_variable = {
        'TestOperation':list_of_TestOperation
    }
    return render(request,'Test&Operation/TestOperationview.html',context_variable)


@csrf_exempt # delection the csrf token detection method 
#method to give path to upload page 
def view_upload(request):
    return render(request, 'image/upload.html') 

@csrf_exempt # delection the csrf token detection method 
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

