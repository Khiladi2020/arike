from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Patient, FamilyDetail, PatientDisease

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

# Family Detail Views


class FamilyDetailForm(ModelForm):
    class Meta:
        model = FamilyDetail
        exclude = ["patient"]
        # fields = '__all__'


class FamilyDetailListView(LoginRequiredMixin, generic.ListView):
    model = FamilyDetail

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return FamilyDetail.objects.filter(patient__pk=patient_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs['patient_id'])
        return context


class FamilyDetailCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = FamilyDetailForm
    template_name = "patient/familydetail_form.html"
    success_url = "/patient/"

    def form_valid(self, form):
        patient_id = self.kwargs["patient_id"]
        form.instance.patient = Patient.objects.get(pk=patient_id)
        return super().form_valid(form)


class FamilyDetailUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = FamilyDetail
    form_class = FamilyDetailForm

    def get_success_url(self):
        patient_id = self.kwargs["patient_id"]
        return reverse_lazy('patient:familydetail_list', args=[patient_id])

# Disease history Views


class PatientDiseaseForm(ModelForm):
    class Meta:
        model = PatientDisease
        exclude = ['patient']


class PatientDiseaseListView(generic.ListView):
    model = PatientDisease

    def get_queryset(self):
        patient_id = self.kwargs["patient_id"]
        return PatientDisease.objects.filter(patient__pk=patient_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fetch patient_id argument from url
        patient_id = self.kwargs["patient_id"]
        context['patient'] = Patient.objects.get(pk=patient_id)
        return context


class PatientDiseaseCreateView(generic.CreateView):
    model = PatientDisease
    form_class = PatientDiseaseForm

    def form_valid(self, form):
        form.instance.patient = Patient.objects.get(
            pk=self.kwargs["patient_id"])
        return super().form_valid(form)

    def get_success_url(self):
        patient_id = self.kwargs["patient_id"]
        return reverse_lazy("patient:patientdisease_list", args=[patient_id])

class PatientDiseaseUpdateView(generic.UpdateView):
    model = PatientDisease
    form_class = PatientDiseaseForm
    template_name = "patient/patientdisease_update.html"

    def get_success_url(self):
        patient_id = self.kwargs["patient_id"]
        return reverse_lazy("patient:patientdisease_list", args=[patient_id])
