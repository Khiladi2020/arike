from django.db import models

# Choices
STATE_CHOICES = (
    ("Rajasthan", "Rajasthan"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Karnataka", "karnataka"),
    ("Maharastra", "Maharastra")
)

LSG_CHOICES = (
    ('Gram Panchayat', 'Gram panchayat'),
    ('Municipality', 'Municipality')
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

STANDARD_TEXT_LENGTH = 80

# Create your models here.


class State(models.Model):
    name = models.CharField(choices=STATE_CHOICES)


class District(models.Model):
    name = models.CharField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class LsgBody(models.Model):
    name = models.CharField()
    kind = models.CharField()
    state = models.ForeignKey(District, on_delete=models.CASCADE)


class Ward(models.Model):
    name = models.CharField(max_length=STANDARD_TEXT_LENGTH)
    number = models.IntegerField()
    lsg_body = models.ForeignKey(LsgBody, on_delete=models.CASCADE)


class Facility(models.Model):
    kind = models.CharField(choices=FACILITY_CHOICES)
    name = models.CharField(max_length=STANDARD_TEXT_LENGTH)
    address = models.TextField()
    pincode = models.IntegerField()
    phone = models.IntegerField()
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
