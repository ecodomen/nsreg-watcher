from django import forms
import validators
import whois


class DomainLookupForm(forms.Form):
    search = forms.CharField(
        label="Домен:",
        max_length=253,
        required=False,)

    def is_valid(self):
        valid = super(DomainLookupForm, self).is_valid()
        if (not validators.domain(self.cleaned_data.get("search"))):
            self.add_error('search', 'Invalid URL')
        else:
            try:
                whois.whois(self.cleaned_data.get("search"))
                self.add_error('search', f"Домен: {self.cleaned_data.get('search')} занят.")
            except whois.parser.PywhoisError:
                self.add_error('search', f"Домен: {self.cleaned_data.get('search')} свободен.")
        return valid
