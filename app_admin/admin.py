from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AppUser, AppUserManager
# Register your models here.
admin.register(AppUser, UserAdmin)