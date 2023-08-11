from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    """
    One-to-one model with user for profile data
    """
    PATIENT = "Patient"
    DOCTOR = "Doctor"
    STAFF = "Staff"
    USER_TYPE_CHOICES = [
        (PATIENT, PATIENT),
        (DOCTOR, DOCTOR),
        (STAFF, STAFF),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=7)
    emergency_contact = models.ForeignKey("EmergencyContact", on_delete=models.SET_NULL, blank=True, null=True)


class EmergencyContact(models.Model):
    FATHER = "Father"
    MOTHER = "Mother"
    SISTER = "Sister"
    BROTHER = "Brother"
    FRIEND = "Friend"
    OTHER = "Other"
    RELATIONSHIP_CHOICES = [
        (FATHER, FATHER),
        (MOTHER, MOTHER),
        (SISTER, SISTER),
        (BROTHER, BROTHER),
        (FRIEND, FRIEND),
        (OTHER, OTHER)
    ]
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    relationship_to_user = models.CharField(choices=RELATIONSHIP_CHOICES, max_length=8)


class HealthFacility(models.Model):
    name = models.CharField(max_length=150)
    street_address = models.CharField(max_length=200)
    region_or_state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    opening_hour = models.ForeignKey("HealthFacilityOpenHour", on_delete=models.SET_NULL, blank=True, null=True)


class HealthFacilityOpenHour(models.Model):
    time_from = models.CharField(max_length=5)
    time_to = models.CharField(max_length=5)
    day_name = models.CharField(max_length=8)


class DoctorSpecialization(models.Model):
    specialization_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
