from django.urls import path
from .views import *

urlpatterns = [
    path('patients/<int:CONTENT_NUMBER>/<int:PAGENO>',view_patient_pagination),
] 