from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Patient

# Create your views here.


class PatientListView(LoginRequiredMixin, generic.ListView):
    # commented this code as thease are deafult values itself
    # template_name = "patient/patient_list.html"
    # context_object_name = "patient_list"
    model = Patient


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Patient


class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Patient
    success_url = "/patient/"
    fields = ["full_name", "date_of_birth", "address",
              "landmark", "phone", "gender", "emergency_phone_number", "ward", "facility"]


class PatientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Patient
    template_name = "patient/patient_update.html"
    success_url = "/patient/"
    fields = ["full_name", "date_of_birth", "address",
              "landmark", "phone", "gender", "emergency_phone_number", "ward", "facility"]
