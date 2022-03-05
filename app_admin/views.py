from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from app_admin.admin import UserChangeForm, UserCreationForm

from .models import AppUser, Facility

# Create your views here.

# Home

def home_page(request):
    return render(request, 'app_admin/home.html', {})

# Profile
class ProfilePageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "app_admin/profile.html"

# Autorization


class AdminAccessRequired(LoginRequiredMixin, PermissionRequiredMixin):
    def has_permission(self):
        if self.request.user.role == "district_admin":
            return True
        return False

    def get_permission_denied_message(self):
        return "Only District Admin's can access this resource."

# FACILITY


class FacilityListView(AdminAccessRequired, generic.ListView):
    model = Facility


class FacilityDetailView(AdminAccessRequired, generic.DetailView):
    model = Facility


class FacilityCreateView(AdminAccessRequired, generic.CreateView):
    model = Facility
    success_url = "/admin/facility/"
    fields = ['kind', 'name', 'address', 'pincode', 'phone', 'ward']


class FacilityUpdateView(AdminAccessRequired, generic.UpdateView):
    model = Facility
    template_name = "app_admin/facility_update.html"
    success_url = "/admin/facility/"
    fields = ['kind', 'name', 'address', 'pincode', 'phone', 'ward']


class FacilityDeleteView(AdminAccessRequired, generic.DeleteView):
    model = Facility
    success_url = "/admin/facility/"

# USERS


class UserListView(AdminAccessRequired, generic.ListView):
    model = AppUser


class UserDetailView(AdminAccessRequired, generic.DetailView):
    model = AppUser


class UserCreateView(AdminAccessRequired, generic.CreateView):
    form_class = UserCreationForm
    template_name = "app_admin/appuser_form.html"
    success_url = "/admin/user/"


class UserUpdateView(AdminAccessRequired, generic.UpdateView):
    model = AppUser
    form_class = UserChangeForm
    template_name = "app_admin/appuser_update.html"
    success_url = "/admin/user/"


class UserDeleteView(AdminAccessRequired, generic.DeleteView):
    model = AppUser
    success_url = "/admin/user/"

# Auth Views


class AuthLoginView(LoginView):
    template_name = "login.html"
