from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Q
from django.contrib import messages

from .models import Price, Registrator
from .forms import CompaniesSortForm, DomainLookupForm

import whois


SORT_FIELD_NAMES = {
    'CN': 'registrator__name',
    'CI': 'registrator__city',
    'RE': 'price_reg',
    'PR': 'price_prolong',
    'PE': 'price_change',

}


def registrator_list(request):
    search = ''
    sort_by = 'id'
    if request.method == "POST":
        if 'search_sub' in request.POST:
            form = CompaniesSortForm(request.POST)
            domain_lookup_form = DomainLookupForm()
            if form.is_valid():
                sort_by = form.cleaned_data['reverse_order'] + SORT_FIELD_NAMES.get(form.cleaned_data['sort_by'], 'name')
                search = form.cleaned_data['search']

        elif 'whois_sub' in request.POST:
            domain_lookup_form = DomainLookupForm(request.POST)
            form = CompaniesSortForm()
            if domain_lookup_form.is_valid():
                domain = domain_lookup_form.cleaned_data.get('domain')
                try:
                    whois.whois(domain)
                    messages.success(request, f"Домен: {domain} занят.")
                except whois.parser.PywhoisError:
                    messages.success(request, f"Домен: {domain} свободен.")
            else:
                messages.error(request, "Недопустимый URL.")

    else:
        form = CompaniesSortForm()
        domain_lookup_form = DomainLookupForm()

    if search:
        companies = Price.objects.filter(Q(registrator__name__icontains=search) | Q(
            registrator__city__icontains=search) | Q(price_reg__icontains=search))
    else:
        companies = Price.objects.filter()

    companies = companies.order_by('registrator_id', '-parse__id')
    companies = Price.objects.filter(id__in=companies).distinct('registrator_id')
    companies = Price.objects.filter(id__in=companies).order_by(sort_by)

    return render(request, 'registrator-list.html', {'companies': companies, 'form': form, 'domain_lookup_form': domain_lookup_form})


def registrator_details(request, id):
    try:
        registrator = Registrator.objects.get(id=id)
        prices = Price.objects.filter(registrator=registrator)
    except Price.DoesNotExist:
        return HttpResponseNotFound(f"Компания с идентификатором {id} в базе не найдена.")
    return render(request, 'registrator-details.html', {'prices': prices, 'registrator': registrator})


def about(request):
    return render(request, 'about-us.html', )


def project_view(request):
    return render(request, 'project.html')
