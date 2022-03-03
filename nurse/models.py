from django.db import models
from django.conf import settings

# from patient.models import Patient
from app_admin.models import AppUser

TEXT_LENGTH = settings.DEFAULT_TEXT_LENGTH
# Create your models here.


class Visit(models.Model):
    palliative_phase = models.CharField(max_length=TEXT_LENGTH)
    blood_pressure = models.CharField(max_length=TEXT_LENGTH)
    pulse = models.CharField(max_length=TEXT_LENGTH)
    general_random_blood_sugar = models.CharField(
        max_length=TEXT_LENGTH)
    personal_hygiene = models.CharField(max_length=TEXT_LENGTH)
    mouth_hygiene = models.CharField(max_length=TEXT_LENGTH)
    pubic_hygiene = models.CharField(max_length=TEXT_LENGTH)
    systemic_examination = models.CharField(max_length=TEXT_LENGTH)
    patient_at_peace = models.BooleanField(default=False)
    pain = models.BooleanField(default=False)
    symptoms = models.CharField(max_length=TEXT_LENGTH)
    note = models.TextField()


class VisitSchedule(models.Model):
    visit_time = models.DateTimeField()
    duration = models.IntegerField()
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)
    nurse = models.ForeignKey(AppUser,on_delete=models.CASCADE)
