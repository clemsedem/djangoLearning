from django.db import models
from city.models import  City


class Locality(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    locality_name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
