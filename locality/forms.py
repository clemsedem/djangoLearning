from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from .models import Locality
from django.utils.translation import gettext_lazy as _
import re
from my_validators import required_field, letters_n_space_only, locality_already_exist


class LocalityForm(ModelForm):
    # locality_name = CharField(
    #     label='Locality',
    #     max_length=20,
    #     validators=[
    #           required_field,
    #           letters_n_space_only,
    #           locality_already_exist
    #       ])


    class Meta:
        model = Locality
        fields = ['locality_name']

    def clean_locality_name(self, *args, **kwargs):
        locality_name = self.cleaned_data.get('locality_name')

        if not locality_name:
            raise ValidationError(_('This field is required'))

        if not re.match("^[a-zA-Z ]*$", locality_name):
            raise ValidationError(_('Letters only'))

        locality = Locality.objects.filter(locality_name__iexact=locality_name, status=True)
        if self.instance:
            locality = locality.exclude(pk=self.instance.pk)

        if locality.exists():
            raise ValidationError(_("Locality already exist"))

        return locality_name