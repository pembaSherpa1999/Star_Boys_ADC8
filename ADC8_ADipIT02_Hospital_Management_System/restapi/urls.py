from django.urls import path
from .views import *

# URL's for getting patients information through ID or NOT using ID
urlpatterns = [
    path('patients/',view_get_post_patient),
    path('patients/<int:ID>',view_getByID_updateByID_deleteByID),
    
] 