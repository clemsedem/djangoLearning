from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import re

from region.models import Region
from city.models import City
from locality.models import Locality
from suburb.models import Suburb


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


def city_already_exist(value):
    print('value value => ' + value)
    city = City.objects.filter(city_name__iexact=value, status=True).exists()
    if not city:
        return value
    else:
        raise ValidationError(_("City already exist"))

def locality_already_exist(value):
    print('value value => ' + value)
    locality = Locality.objects.filter(locality_name__iexact=value, status=True)

    if locality.exists():
        raise ValidationError(_("Locality already exist"))

    return  value

def suburb_already_exist(value):
    print('value value => ' + value)
    suburb= Suburb.objects.filter(suburb_name__iexact=value, status=True).exists()
    if not suburb:
        return value
    else:
        raise ValidationError(_("Suburb already exist"))