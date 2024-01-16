from django.shortcuts import render
from .forms import DomainLookupForm
import whois


def domain_lookup(request):
    if request.method == "POST":
        form = DomainLookupForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            results = ""
    else:
        form = DomainLookupForm()
        search = ''
        results = ''

    if search:
        try:
            whois.whois(search)
            results = f"Домен: {search} занят."
        except whois.parser.PywhoisError:
            results = f"Домен: {search} свободен."

    return render(request, 'domain-lookup-details.html', {'results': results, 'form': form})
