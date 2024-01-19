from django import forms

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


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Ваше Имя'})
        )
    contact = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Телефон или email'})
        )
    speciality = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Специальность'})
        )
    message = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Сообщение'})
        )
