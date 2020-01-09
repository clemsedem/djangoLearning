import uuid

from django.db import models
from city.models import City


class Locality(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    locality_name = models.CharField(max_length=20)
    ref = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.locality_name = self.locality_name.lower()
        return super(Locality, self).save(*args, **kwargs)
