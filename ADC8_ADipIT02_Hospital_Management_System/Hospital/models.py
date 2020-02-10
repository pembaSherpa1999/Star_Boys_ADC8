from django.db import models
from django.contrib.auth.models import User

# Model used for Staff Log
class StaffLog(models.Model):
    Staffname = models.ManyToManyField(User,blank=True,related_name="user")
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
     
    def __str__(self):
        return self.Staffname +""+ self.email+""+ self.password

    
# Model used for Hospital

class hospital(models.Model):
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=20)
    Contact = models.IntegerField()

    def __str__(self):
        return self.Name + ""+ self.Address +""+str(self.Contact)
    

# Model used for Doctor

class doctor(models.Model):
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=20)
    Contact = models.IntegerField()
    department = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
 
    def __str__(self):
        return self.Name +""+ self.Address +""+ str(self.Contact )+""+ self.department +""+self.education


# Model used for Nurse

class Nurse(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=20)
    PhoneNo = models.IntegerField()
   
    def __str__(self):
        return self.Name+""+self.Address+""+str(self.PhoneNo)


# Model used for Patient Pictures

class patientPic(models.Model):
    pictureName=models.CharField(max_length=25)
    profilePic =models.ImageField(upload_to ="")
    aboutPic=models.CharField(max_length=300)

# Model used for Patient

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
    
    
    #testing of patient

    def patient_name_blank_check(self):
        if self.patientName == "":
            return False
        else:
            return True

    
    # Model used for listing patient list
    def patient_patient_list_check(self):
        list_of_patients =patient.objects.all().count()
        return list_of_patients   
    
    #Function for checking male count 
    def patient_patient_malecount_check(self):
        patient_malecount = patient.objects.filter(patientSex__contains="male").count()
        return patient_malecount

    #Function for checking Female count 

    def patient_patient_femalecount_check(self):
        patient_femalecount = patient.objects.filter(patientSex__contains="female").count()
        return patient_femalecount
    
    #Function for checking Address 

    def patient_address_check(self):
        class_variables = ['KTM','POK']
        for address in class_variables:
            if self.patientAddress == address:
                return True
            else:
                return False



# Model used for Appointment

class Appointment(models.Model):
    patientName = models.CharField(max_length=200)
    doctorName = models.CharField(max_length=200)
    Date = models.DateField(max_length=100)
    Time = models.TimeField(max_length=100)
    
    
    
    def __str_(self):
        return  self.patientName +" "+ self.Date +" "+ self.Time+""+ self.doctorName
    


# Model used for Department

class Department(models.Model):
    depName = models.CharField(max_length=200)
    doctorID = models.IntegerField()
    
    def __str__(self):
        return  self.depName +""+ str(self.doctorID)



# Model used for Person

class Person(models.Model):
    personName = models.CharField(max_length=100)
    types = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.personName+""+self.types


# Model used for Receptionist

class Receptionist(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    def  __str__(self):
        return self.Name+" "+self.Address


# Model used for Rooms

class Rooms(models.Model):
    RoomNO = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.RoomNO)+""+self.location



# Model used for TestOperation

class TestOperation(models.Model):
    PatientID = models.CharField(max_length=254)
    PatientName =models.CharField(max_length=254)
    prescribeMedicine = models.CharField(max_length=254)
    prescribeTratment = models.CharField(max_length=200)
    report = models.CharField(max_length=200)
  
    def __str__(self):
        return str(self.PatientID)+""+self.prescribeMedicine+""+self.prescribeTratment+""+self.report



# Model used for Staff

class Staff(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=10)
    Position = models.CharField(max_length=20)

    def __str__(self):
         return self.Name +""+ self.Address+""+ self.Position


# Model used for Bill

class Bill(models.Model):
    BillNo = models.IntegerField()
    PatientName = models.CharField(max_length=10)
    Amount = models.IntegerField()
    
    def __str__(self):
        return str(self.BillNo) +""+ self.PatientName +""+str(self.Amount)
        