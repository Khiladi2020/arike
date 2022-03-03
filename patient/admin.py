from django.contrib import admin

from .models import (Disease, FamilDetail, Patient, PatientDisease, Treatment,
                     TreatmentNotes)

# Register your models here.
admin.site.register([Patient, FamilDetail, Disease,
                    PatientDisease, Treatment, TreatmentNotes])
