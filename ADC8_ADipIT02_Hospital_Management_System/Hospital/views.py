from django.shortcuts import render
from .models import *
from django.views.generic import ListView
# Create your views here.
class SearchPatientView(ListView):
    model = patient
    template_name = 'search_patient.html'

    def get_quertset(self):
       query = self.request.GET.get('patient name')
       patient_list = patient.objects.filter(
           Q(name__icontains=query) | Q(address__icontains=query)
       )
       return patient_list

def uploadImage(request):
    return render(request, 'upload.html')

def upload(request):
    print("image uploading .. .. .. . .")
    picture  = print(request.FILES['patient image'])
    photo = patient(profile = picture)
    photo.save()
    return render(request, 'upload.html')