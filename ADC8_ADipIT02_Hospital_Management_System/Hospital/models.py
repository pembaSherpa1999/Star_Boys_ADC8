
# model used for Permission

from django.db import models
from django.contrib.auth.models import User

class patient(models.Model):
    patientName = models.CharField(max_length=250)
    patientAddress = models.CharField(max_length=20)
    patientPhoneNo = models.IntegerField()
    patientAge = models.IntegerField()
    patientSex = models.CharField(max_length=20)
    
    
    def __str__(self):  
        return  self.patientName +""+ self.patientAddress +""+str(self.patientPhoneNo)+""+ str(self.patientAge)
    
    def is_valid_patient(self):

        return (self.patientName !=self.patientSex) and (self.patientAge >=0)