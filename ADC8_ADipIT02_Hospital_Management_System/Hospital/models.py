from django.db import models

# Create your models here.
class patient(models.Model):
    profile = models.ImageField(upload_to= "profile")