from re import L, template
import django
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from app_admin.admin import UserChangeForm, UserCreationForm

from .models import AppUser, Facility

# Create your views here.


def home_page(request):
    return render(request, 'app_admin/home.html', {})
    # return HttpResponse("coolie gyzs")


def login_page(request):
    return render(request, 'login.html', {})


# FACILITY
class FacilityListView(LoginRequiredMixin,generic.ListView):
    model = Facility


class FacilityDetailView(generic.DetailView):
    model = Facility


class FacilityCreateView(generic.CreateView):
    model = Facility
    success_url = "/admin/facility/"
    fields = ['kind', 'name', 'address', 'pincode', 'phone', 'ward']


class FacilityUpdateView(generic.UpdateView):
    model = Facility
    template_name = "app_admin/facility_update.html"
    success_url = "/admin/facility/"
    fields = ['kind', 'name', 'address', 'pincode', 'phone', 'ward']


class FacilityDeleteView(generic.DeleteView):
    model = Facility
    success_url = "/admin/facility/"

# USERS


class UserListView(generic.ListView):
    model = AppUser


class UserDetailView(generic.DetailView):
    model = AppUser


class UserCreateView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "app_admin/appuser_form.html"
    success_url = "/admin/user/"


class UserUpdateView(generic.UpdateView):
    model = AppUser
    form_class = UserChangeForm
    template_name = "app_admin/appuser_update.html"
    success_url = "/admin/user/"


class UserDeleteView(generic.DeleteView):
    model = AppUser
    success_url = "/admin/user/"

# Auth Views
class AuthLoginView(LoginView):
    template_name = "login.html"
