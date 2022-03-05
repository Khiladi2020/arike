from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import AppUser, District, Facility, LsgBody, State, Ward

# User Creation Form
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation",widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ('fullname','email','role','phone','district','facility')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # save the provided password in hashed form
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# User change form
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = AppUser
        fields = ('fullname','email','role','phone','district','facility','password')

# Register Custom User model with Django Admin
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'phone', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('fullname','role','phone','district','facility')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)

# Register your models here.
admin.site.register(AppUser,UserAdmin)

# Unregister Group model becouse we are not using django's
# built in permissions
admin.site.unregister(Group)

# admin.site.register([AppUser, State, District, Ward, Facility,LsgBody])
