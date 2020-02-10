from django.test import TestCase
from .models import patient

# Create your tests here.

class patientModelTestCase(TestCase):
    def test_patient_name_blank_check(self):
        patient1= patient.objects.create(patientName="ram shrestha",patientAddress="shamakoshi",patientPhoneNo=9807656753,patientAge=20,patientSex="male")
        self.assertTrue(patient1.patient_name_blank_check())


    def test_patient_patient_list_check(self):
        patient2= patient.objects.create(patientName="kritan shrestha",patientAddress="shamakoshi",patientPhoneNo=9807656753,patientAge=20,patientSex="male")
        self.assertEqual(patient2.patient_patient_list_check(),1)
    
    def test_patient_patient_malecount_check(self):
        patient3= patient.objects.create(patientName="kritan shrestha",patientAddress="shamakoshi",patientPhoneNo=9807656753,patientAge=20,patientSex="male")
        self.assertEqual(patient3.patient_patient_malecount_check(),1)
    
    def test_patient_patient_femalecount_check(self):
        patient4= patient.objects.create(patientName="kritan shrestha",patientAddress="shamakoshi",patientPhoneNo=9807656753,patientAge=20,patientSex="female")
        self.assertEqual(patient4.patient_patient_femalecount_check(),1)
   

    def test_patient_address_check(self):
        patient5= patient.objects.create(patientName="kritan shrestha",patientAddress="KTM",patientPhoneNo=9807656753,patientAge=20,patientSex="female")
        self.assertTrue(patient5.patient_address_check())
   


