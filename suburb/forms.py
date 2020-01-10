import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from .models import Suburb
from django.utils.translation import gettext_lazy as _
from my_validators import required_field, letters_n_space_only, suburb_already_exist


class SuburbForm(ModelForm):
    # suburb_name = CharField(
    #     label='Suburb',
    #     max_length=20,
    #     validators=[
    #         required_field,
    #         letters_n_space_only,
    #         suburb_already_exist
    #     ])


    class Meta:
        model = Suburb
        fields = ['suburb_name']

    def clean_suburb_name(self, *args, **kwargs):
        suburb_name = self.cleaned_data.get('suburb_name')

        if not suburb_name:
            raise ValidationError(_('This field is required'))

        if not re.match("^[a-zA-Z ]*$", suburb_name):
            raise ValidationError(_('Letters only'))

        suburb = Suburb.objects.filter(suburb_name__iexact=suburb_name, status=True)
        if self.instance:
            suburb = suburb.exclude(pk=self.instance.pk)

        if suburb.exists():
            raise ValidationError(_("Suburb name already exist"))

        return suburb_name
