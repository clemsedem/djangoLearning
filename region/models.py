import uuid
from django.db import models


class Region(models.Model):
    region_name = models.CharField(max_length=30)
    ref = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.region_name = self.region_name.lower()
        return super(Region, self).save(*args, **kwargs)
