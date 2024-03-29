from django.db import models
from django.conf import settings

from app_admin.models import Facility, AppUser

TEXT_LENGTH = settings.DEFAULT_TEXT_LENGTH

# Create your models here.
GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female")
)


class Patient(models.Model):
    full_name = models.CharField(max_length=TEXT_LENGTH)
    date_of_birth = models.DateField()
    address = models.TextField()
    landmark = models.CharField(max_length=TEXT_LENGTH, blank=True)
    phone = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=TEXT_LENGTH)
    emergency_phone_number = models.IntegerField()
    expired_time = models.DateTimeField(null=True, blank=True)
    ward = models.CharField(max_length=TEXT_LENGTH)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} -> {self.phone}"


class FamilyDetail(models.Model):
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

    def __str__(self):
        return f"{self.full_name} -> {self.phone}"


class Disease(models.Model):
    name = models.CharField(max_length=TEXT_LENGTH)
    icds_code = models.CharField(max_length=TEXT_LENGTH)

    def __str__(self):
        return self.name


class PatientDisease(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f"{self.patient} -> {self.disease}"

class VisitSchedule(models.Model):
    visit_time = models.DateTimeField()
    duration = models.IntegerField()
    visit_completed = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse = models.ForeignKey(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient} -> {self.nurse}"

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
    visit_schedule = models.ForeignKey(VisitSchedule, on_delete=models.CASCADE)

    def __str__(self):
        return self.palliative_phase




class Treatment(models.Model):
    description = models.TextField()
    care_type = models.CharField(max_length=TEXT_LENGTH)
    care_sub_type = models.CharField(max_length=TEXT_LENGTH)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient


class TreatmentNotes(models.Model):
    note = models.TextField()
    description = models.TextField()
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)

    def __str__(self):
        return self.treatment
