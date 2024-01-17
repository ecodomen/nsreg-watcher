from django.shortcuts import render
from django.contrib import messages

from .forms import DomainLookupForm

import whois


def domain_lookup(request):
    if request.method == "POST":
        form = DomainLookupForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('search')
            try:
                whois.whois(search)
                messages.success(request, f"Домен: {search} занят.")
            except whois.parser.PywhoisError:
                messages.success(request, f"Домен: {search} свободен.")
        else:
            messages.error(request, "Недопустимый URL.")
    else:
        form = DomainLookupForm()

    # return render(request, 'registrator-list.html', {'form': form})
    return render(request, 'domain-lookup-details.html', {'form': form})
