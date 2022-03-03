from django.db import models
from django.conf import settings

from app_admin.models import Facility
from nurse.models import Visit

TEXT_LENGTH = settings.DEFAULT_TEXT_LENGTH

# Create your models here.


class Patient(models.Model):
    full_name = models.CharField(max_length=TEXT_LENGTH)
    date_of_birth = models.DateField()
    address = models.TextField()
    landmark = models.CharField(max_length=TEXT_LENGTH)
    phone = models.IntegerField()
    gender = models.CharField(max_length=TEXT_LENGTH)
    emergency_phone_number = models.IntegerField()
    expired_time = models.DateTimeField()
    ward = models.CharField(max_length=TEXT_LENGTH)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)


class FamilDetail(models.Model):
    full_name = models.CharField(max_length=TEXT_LENGTH)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    email = models.CharField(max_length=TEXT_LENGTH)
    relation = models.CharField(max_length=TEXT_LENGTH)
    address = models.TextField()
    education = models.CharField(max_length=TEXT_LENGTH)
    occupation = models.CharField(max_length=TEXT_LENGTH)
    remarks = models.TextField()
    is_primary = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Disease(models.Model):
    name = models.CharField(max_length=TEXT_LENGTH)
    icds_code = models.CharField(max_length=TEXT_LENGTH)


class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    note = models.TextField()


class Treatment(models.Model):
    description = models.TextField()
    care_type = models.CharField(max_length=TEXT_LENGTH)
    care_sub_type = models.CharField(max_length=TEXT_LENGTH)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


class TreatmentNotes(models.Model):
    note = models.TextField()
    description = models.TextField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
