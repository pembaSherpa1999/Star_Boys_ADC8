#please before running this file install Pillow  for using image fields
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StaffLog(models.Model):
    Staffname = models.ManyToManyField(User,blank=True,related_name="user")
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
     
    def __str__(self):
        return self.Staffname +""+ self.email+""+ self.password

    
# Create your models here.
class hospital(models.Model):
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=20)
    Contact = models.IntegerField()
    
    def __str__(self):
        return self.Name + ""+ self.Address +""+str(self.Contact)
    


# Create your models here.
class doctor(models.Model):
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=20)
    Contact = models.IntegerField()
    department = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
 
    def __str__(self):
        return self.Name +""+ self.Address +""+ str(self.Contact )+""+ self.department +""+self.education


# Create your models here.
class Nurse(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=20)
    PhoneNo = models.IntegerField()
   
    def __str__(self):
        return self.Name+""+self.Address+""+str(self.PhoneNo)


# Create your models here.

class patientPic(models.Model):
    pictureName=models.CharField(max_length=25)
    profilePic =models.ImageField(upload_to ="")
    aboutPic=models.CharField(max_length=300)

class patient(models.Model):
    patientName = models.CharField(max_length=250)
    patientAddress = models.CharField(max_length=20)
    patientPhoneNo = models.IntegerField()
    patientAge = models.IntegerField()
    patientSex = models.CharField(max_length=20)
    
    
    def __str__(self):  
        return  self.patientName +""+ self.patientAddress +""+str(self.patientPhoneNo)+""+ str(self.patientAge)
    


# Create your models here.
class Rooms(models.Model):
    RoomNO = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.RoomNO)+""+self.location

# Create  models to store assigned room detail
class Assigned_Room(models.Model):
    RoomNo = models.ForeignKey(Rooms,on_delete=models.CASCADE,related_name="RoomNo")
    patientName = models.ManyToManyField(patient)

    def __str__(self):  
        return  str(self.RoomNO) +""+ self.patientName
    

# Create your models here.
class Appointment(models.Model):
    patientName = models.CharField(max_length=200)
    doctorName = models.CharField(max_length=200)
    Date = models.DateField(max_length=100)
    Time = models.TimeField(max_length=100)
    
    
    
    def __str_(self):
        return  self.patientName +" "+ self.Date +" "+ self.Time+""+ self.doctorName
    


# Create your models here.
class Person(models.Model):
    personName = models.CharField(max_length=100)
    types = models.CharField(max_length=200)
   
    
    def __str__(self):
        return self.personName+""+self.types


# Create your models here.
class Receptionist(models.Model):
    Name = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    def  __str__(self):
        return self.Name+" "+self.Address




# Create your models here.
class TestOperation(models.Model):
    PatientID = models.CharField(max_length=254)
    PatientName =models.CharField(max_length=254)
    prescribeMedicine = models.CharField(max_length=254)
    prescribeTratment = models.CharField(max_length=200)
    report = models.CharField(max_length=200)
  
    def __str__(self):
        return str(self.PatientID)+""+self.prescribeMedicine+""+self.prescribeTratment+""+self.report



# Create your models here.
class Staff(models.Model):
    Name = models.ForeignKey(Person,on_delete=models.CASCADE)
    Address = models.CharField(max_length=10)
    Position = models.CharField(max_length=20)

    def __str__(self):
         return self.Name +""+ self.Address+""+ self.Position


# Create your models here.
class Bill(models.Model):
    BillNo = models.IntegerField()
    PatientName = models.CharField(max_length=20)
    Amount = models.IntegerField()
    
    def __str__(self):
        return str(self.BillNo) +""+ self.PatientName +""+str(self.Amount)

# Create your models here.
class Department(models.Model):
    depName = models.CharField(max_length=200)
    Staff = models.ManyToManyField(StaffLog,blank=True,related_name="staffName")
    
    def __str__(self):
        return  self.depName +""+ str(self.doctorID)
