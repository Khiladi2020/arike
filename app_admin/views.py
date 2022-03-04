from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import AppUser, Facility

# Create your views here.


def home_page(request):
    return render(request, 'app_admin/home.html', {})
    # return HttpResponse("coolie gyzs")


def index(request):
    return render(request, 'base.html', {})


# FACILITY
class FacilityListView(generic.ListView):
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
    model = AppUser
    success_url = "/admin/user/"
    fields = ['fullname', 'role', 'email', 'phone',
              'district', 'facility', 'password']


class UserUpdateView(generic.UpdateView):
    model = AppUser
    template_name = "app_admin/appuser_update.html"
    success_url = "/admin/user/"
    fields = ['fullname', 'role', 'email', 'phone',
              'district', 'facility', 'password']


class UserDeleteView(generic.DeleteView):
    model = AppUser
    success_url = "/admin/user/"
