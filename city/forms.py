import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from .models import City
from django.utils.translation import gettext_lazy as _
from my_validators import required_field, letters_n_space_only, city_already_exist


class CityForm(ModelForm):
    # city_name = CharField(label='City',
    #                       validators=[
    #                           required_field,
    #                           letters_n_space_only,
    #                           city_already_exist
    #                       ])


    class Meta:
        model = City
        fields = ['city_name']
        labels = {
            'city_name': _('City')
        }

    def clean_city_name(self, *args, **kwargs):
        city_name = self.cleaned_data.get('city_name')

        # required validation
        if not city_name:
            raise ValidationError(_('This field is required'))

        #string only
        if not re.match("^[a-zA-Z ]*$", city_name):
            raise ValidationError(_('Letters only'))

        # City already exists
        city = City.objects.filter(city_name__iexact=city_name, status=True)

        if self.instance:
            city = city.exclude(pk=self.instance.pk)

        if city.exists():
            raise ValidationError(_("City already exist"))

        return city_name