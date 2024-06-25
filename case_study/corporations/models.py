# Create your models here.
from django.db import models


class Corporation(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)  # null=True is not needed because it is a text field
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    corporation = models.ForeignKey(Corporation, related_name="locations", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=15)  # zip_code instead of zip because zip is a python built-in function.
    country = models.CharField(max_length=255)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)  # precision corresponds to one meter
    latitude = models.DecimalField(max_digits=8, decimal_places=5)  # precision corresponds to one meter

    def __str__(self) -> str:
        return f"{self.name} - {self.corporation.name}"
