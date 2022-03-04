from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

# Choices

LSG_CHOICES = (
    (1, "Grama Panchayath"),
    (2, "Block Panchayath"),
    (3, "District Panchayath"),
    (4, "Nagar Panchayath"),
    (10, "Municipality"),
    (20, "Corporation"),
    (50, "Others"),
)


FACILITY_CHOICES = (
    ('PHC', 'PHC'),
    ('CHC', 'CHC')
)

ROLE_CHOICES = (
    ("district_admin", "district_admin"),
    ("primary_nurse", "primary_nurse"),
    ("secondary_nurse", "secondary_nurse")
)

TEXT_LENGTH = settings.DEFAULT_TEXT_LENGTH

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=TEXT_LENGTH)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=TEXT_LENGTH)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.state}"


class LsgBody(models.Model):
    name = models.CharField(max_length=TEXT_LENGTH)
    kind = models.IntegerField(choices=LSG_CHOICES)
    lsg_body_code = models.CharField(max_length=TEXT_LENGTH)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.district} -> {self.name}"


class Ward(models.Model):
    name = models.CharField(max_length=TEXT_LENGTH)
    number = models.IntegerField()
    lsg_body = models.ForeignKey(LsgBody, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Facility(models.Model):
    kind = models.CharField(choices=FACILITY_CHOICES, max_length=TEXT_LENGTH)
    name = models.CharField(max_length=TEXT_LENGTH)
    address = models.TextField()
    pincode = models.IntegerField()
    phone = models.IntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.kind}"

# Custom User Manager


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

# custom User Model


class AppUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=TEXT_LENGTH, blank=True)
    role = models.CharField(choices=ROLE_CHOICES,
                            max_length=TEXT_LENGTH, default=ROLE_CHOICES[0][0])
    email = models.EmailField(unique=True)
    phone = models.IntegerField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True)
    facility = models.ForeignKey(
        Facility, on_delete=models.CASCADE, blank=True, null=True)
    # additional fields
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"
    objects = AppUserManager()
