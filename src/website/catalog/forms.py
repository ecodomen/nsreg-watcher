from django import forms
from django.core.validators import RegexValidator

URL_VALIDATOR_MESSAGE = 'Недопустимый URL.'
URL_VALIDATOR = RegexValidator(regex=r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[a-zA-Z0-9._%+-]*)*$', message=URL_VALIDATOR_MESSAGE)

SORT_BY_CHOICES = [
    ("CN", "Имя компании"),
    ("CI", "Город"),
    ("RE", "Регистрация домена"),
    ("PR", "Продление домена"),
    ("PE", "Перенос домена"),
]

SORT_IN_REVERSE_ORDER = [
    ('', "возрастания"),
    ('-', "убывания"),
]


class CompaniesSortForm(forms.Form):
    sort_by = forms.ChoiceField(
        label="Сортировать по",
        choices=SORT_BY_CHOICES,
    )
    reverse_order = forms.ChoiceField(
        label="В порядке",
        choices=SORT_IN_REVERSE_ORDER,
        required=False,
    )
    search = forms.CharField(
        label="Поиск",
        max_length=50,
        required=False,)


class DomainLookupForm(forms.Form):
    domain = forms.CharField(
        label="Домен:",
        max_length=253,
        required=False,
        validators=[URL_VALIDATOR]
        )
