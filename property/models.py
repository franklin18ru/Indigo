from django.db import models
from realtor.models import Realtors

# Create your models here.


class Properties(models.Model):
    streetName = models.CharField(max_length=255)
    price = models.FloatField()
    propValue = models.PositiveIntegerField()
    fireInsurance = models.PositiveIntegerField()
    squareMeter = models.FloatField()
    rooms = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    zip = models.CharField(max_length=3)
    description = models.CharField(max_length=999)
    shortDescription = models.CharField(max_length=255)
    realtor = models.ForeignKey(Realtors, on_delete=models.CASCADE)
    zone = models.CharField(max_length=255, default="default")


class PropertyImage(models.Model):
    propertyId = models.ForeignKey(Properties, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)


class PropertyZoneArea(models.Model):
    zip = models.CharField(max_length=3)
    area = models.CharField(max_length=255)
    region = models.CharField(max_length=255)

