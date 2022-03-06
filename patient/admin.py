from django.contrib import admin

from .models import (Disease, FamilyDetail, Patient, PatientDisease, Treatment,
                     TreatmentNotes)

# Register your models here.
admin.site.register([Patient, FamilyDetail, Disease,
                    PatientDisease, Treatment, TreatmentNotes])
