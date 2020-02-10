from django.urls import path
from .views import *

urlpatterns = [
    path('patients/',view_get_post_patient),
    path('patients/<int:ID>',view_getByID_updateByID_deleteByID),
    path('patients/<int:CONTENT_NUMBER>/<int:PAGENO>',view_patient_pagination),
] 