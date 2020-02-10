from django.urls import path
from .views import *

# URL's for DELETION and UPDATING patients information
urlpatterns = [
    path('patientdelete/<int:ID>',view_patient_delete),
    path('patientupdate/<int:ID>',view_patient_update),
]


