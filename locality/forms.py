from django.forms import ModelForm, CharField
from .models import Locality
from django.utils.translation import gettext_lazy as _
from my_validators import required_field, letters_n_space_only, locality_already_exist


class LocalityForm(ModelForm):
    locality_name = CharField(
        label='Locality',
        max_length=20,
        validators=[
              required_field,
              letters_n_space_only,
              locality_already_exist
          ])


    class Meta:
        model = Locality
        fields = ['locality_name']
