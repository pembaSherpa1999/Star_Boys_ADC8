"""django_first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

# this is the url of Hospital of all views
urlpatterns = [
    
    path('',view_home),
    path('Home',view_home),
    path('patient/',view_patient),
    path('patient/save',view_patientdata_save),
    path('patientdata/',view_patient_lists),
    
    path('patientdelete/<int:ID>',view_patient_delete),
    path('patientupdate/<int:ID>',view_update),
    path('patientupdate/save',view_patient_update),

    path('doctor/',view_add_doctor_detail),
    path('doctor/save',view_doctordata_save),
    path('doctordata/',view_doctor_lists),

    path('appointment/',view_appointment_details),
    path('appointment/save',view_appointment_save),
    path('appointmentdata/', view_appointment_lists),

    path('bill/',view_billing_details),
    path('bill/save',view_billdata_save),
    path('billdata/',view_bill_lists),
    
    path('uploadimage/',view_upload),
    path('uploadimage/upload',view_uploadImage),
    path('image/',view_showimage),
    
    path('signup/',view_register_staff),
    path('login/',view_login_staff),
    path('logout/',view_logout),
    
    path('test/',view_Testoperation_details),
    path('test/save', view_testdata_save),
    path('testdata/',view_test_lists),
    path('search/', view_search_page),
   
   
]