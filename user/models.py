from django.db import models
from property.models import PropertyZoneArea


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Buyers(models.Model):
    name = models.CharField(max_length=255)
    ssn = models.PositiveIntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.ForeignKey(PropertyZoneArea, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
