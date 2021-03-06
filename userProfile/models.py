from django.contrib.auth.models import User
from django.db import models
from property.models import Properties



# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Properties)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)