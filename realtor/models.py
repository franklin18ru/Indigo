from django.db import models

# Create your models here.

class Positions(models.Model):
    name = models.CharField(max_length=255)


class Realtors(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=999)
    password = models.CharField(max_length=255)
    positions = models.ManyToManyField(Positions)
    image = models.CharField(max_length=255)


class SoldProperty(models.Model):
    streetName = models.CharField(max_length=255)
    zip = models.CharField(max_length=3)
    price = models.PositiveIntegerField()
    realtor = models.ForeignKey(Realtors, on_delete=models.CASCADE)

