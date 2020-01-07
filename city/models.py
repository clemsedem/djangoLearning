from django.db import models
from region.models import Region


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
