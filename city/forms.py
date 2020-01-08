from django.forms import ModelForm, CharField, HiddenInput
from .models import City
from django.utils.translation import gettext_lazy as _
from my_validators import required_field, letters_n_space_only

class CityForm(ModelForm):
    city_name = CharField(label='City', validators=[required_field, letters_n_space_only])

    class Meta:
        model = City
        fields = ['city_name']
        labels = {
            'city_name': _('City')
        }