from django.db import models

from admin.models import Facility
from nurse.models import Visit

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    address= models.TextField()
    landmark=models.CharField()
    phone = models.IntegerField()
    gender = models.CharField()
    emergency_phone_number = models.IntegerField()
    expired_time = models.DateTimeField()
    ward = models.CharField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

class FamilDetail(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.CharField()
    relation = models.CharField()
    address = models.TextField()
    education = models.CharField()
    occupation = models.CharField()
    remarks = models.TextField()
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class Disease(models.Model):
    name = models.CharField()
    icds_code = models.CharField()

class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    note = models.TextField()

class Treatment(models.Model):
    description = models.TextField()
    care_type = models.CharField()
    care_sub_type = models.CharField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class TreatmentNotes(models.Model):
    note = models.TextField()
    description = models.TextField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)