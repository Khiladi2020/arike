from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'base.html',{})
    # return HttpResponse("coolie gyzs")
    
def index(request):
    return HttpResponse("admin view")
