from django.forms import ModelForm, CharField
from .models import City
from django.utils.translation import gettext_lazy as _
from my_validators import required_field, letters_n_space_only, city_already_exist


class CityForm(ModelForm):
    city_name = CharField(label='City',
                          validators=[
                              required_field,
                              letters_n_space_only,
                              city_already_exist
                          ])


    class Meta:
        model = City
        fields = ['city_name']
        labels = {
            'city_name': _('City')
        }
