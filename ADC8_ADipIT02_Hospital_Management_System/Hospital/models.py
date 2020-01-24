from django.db import models

# Create your models here.

 
class StaffLog(models.Model):
    Staffname = models.CharField(max_length=30)
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
class Appointment(models.Model):
    patientName = models.CharField(max_length=100)
    doctorName = models.CharField(max_length=100)
    Date = models.DateField(max_length=100)
    Time = models.TimeField(auto_now_add=True, blank=True)
    
    
    def __str_(self):
        return self.Date +" "+ self.Time+""+ self.doctorName
    




# Create your models here.
class Department(models.Model):
   
    depName = models.CharField(max_length=200)
    doctorID = models.IntegerField()
    
    def __str__(self):
        return  self.depName +""+ str(self.doctorID)


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
    profilePic =models.ImageField(upload_to ="profiles")

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
class Rooms(models.Model):
    RoomNO = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.RoomNO)+""+self.location



# Create your models here.
class TestOperation(models.Model):
    PatientID = models.IntegerField(max_length=12)
    PatientName = models.CharField(max_length=254)
    Sex=models.CharField(max_length=254)
    prescribeMedicine = models.CharField(max_length=254)
    prescribeTratment = models.CharField(max_length=200)
    report = models.CharField(max_length=200)
  
    def __str__(self):
        return str(self.PatientID)+""+self.prescribeMedicine+""+self.prescribeTratment+""+self.report



# Create your models here.
class Staff(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=10)
    Position = models.CharField(max_length=20)

    def __str__(self):
         return self.Name +""+ self.Address+""+ self.Position


# Create your models here.
class Bill(models.Model):
    BillNo = models.IntegerField()
    PatientName = models.CharField(max_length=10)
    Amount = models.IntegerField()
    
    def __str__(self):
        return str(self.BillNo) +""+ self.PatientName +""+str(self.Amount)
        