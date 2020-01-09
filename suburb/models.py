from django.db import models
from locality.models import Locality
import uuid

class Suburb(models.Model):
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    suburb_name = models.CharField(max_length=20)
    ref = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.suburb_name = self.suburb_name.lower()
        return super(Suburb, self).save(*args, **kwargs)
