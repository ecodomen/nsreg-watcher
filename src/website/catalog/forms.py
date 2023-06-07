from django import forms

SORT_BY_CHOICES = [
    ("CN", "Имя компании"),
    ("CI", "Город"),
    ("RE", "Регистрация домена"),
    ("PR", "Продление домена"),
    ("PE", "Перенос домена"),

    
]

class CompaniesSortForm(forms.Form):
    sort_by = forms.ChoiceField(
        label="Сортировать по", 
        choices=SORT_BY_CHOICES,
    )
    search = forms.CharField(
        label="Поиск",
        max_length=50,
        required=False,)