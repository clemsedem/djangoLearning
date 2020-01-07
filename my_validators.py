from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re

from region.models import Region
from django.db import connection


def letters_n_space_only(value):
    if not re.match("^[a-zA-Z ]*$", value):
        raise ValidationError(_('Letters only'))
    else:
        return value


def required_field(value):
    if not value:
        raise ValidationError(_('This field is required'))
    else:
        return value


def region_already_exist(value):
    region = Region.objects.filter(region_name__iexact=value, status=True).exists()
    print(region)
    if not region:
        return value
    else:
        raise ValidationError(_("Region already exist"))
