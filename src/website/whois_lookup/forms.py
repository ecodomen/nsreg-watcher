from django import forms
from django.core.validators import RegexValidator

URL_VALIDATOR_MESSAGE = 'Недопустимый URL.'
URL_VALIDATOR = RegexValidator(regex=r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[a-zA-Z0-9._%+-]*)*$', message=URL_VALIDATOR_MESSAGE)


class DomainLookupForm(forms.Form):
    search = forms.CharField(
        label="Домен:",
        max_length=253,
        required=False, validators=[URL_VALIDATOR])
