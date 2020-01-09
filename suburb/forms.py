from django.forms import ModelForm, CharField
from .models import Suburb
from django.utils.translation import gettext_lazy as _
from my_validators import required_field, letters_n_space_only, suburb_already_exist


class SuburbForm(ModelForm):
    suburb_name = CharField(
        label='Suburb',
        max_length=20,
        validators=[
            required_field,
            letters_n_space_only,
            suburb_already_exist
        ])


    class Meta:
        model = Suburb
        fields = ['suburb_name']
