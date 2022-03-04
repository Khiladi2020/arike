from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Facility

# Create your views here.


def home_page(request):
    return render(request, 'base.html', {})
    # return HttpResponse("coolie gyzs")


def index(request):
    return render(request, 'base.html', {})


class FacilityListView(generic.ListView):
    model = Facility


class FacilityDetailView(generic.DetailView):
    model = Facility


class FacilityCreateView(generic.CreateView):
    model = Facility
    success_url = "/admin/facility/"
    fields = ['kind', 'name', 'address', 'pincode', 'phone', 'ward']
