from django.urls import path
from .views import *

urlpatterns = [
    path('patientdelete/<int:ID>',view_patient_delete),
    path('patientupdate/<int:ID>',view_patient_update),
]


