from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUser, District, Facility, LsgBody, State, Ward

# Register your models here.
admin.site.register([AppUser, State, District, Ward, Facility,LsgBody])
