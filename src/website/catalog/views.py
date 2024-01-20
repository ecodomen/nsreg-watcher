from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Q

from .models import Price, Registrator, TeamMember
from .forms import CompaniesSortForm, ContactForm


SORT_FIELD_NAMES = {
    'CN': 'registrator__name',
    'CI': 'registrator__city',
    'RE': 'price_reg',
    'PR': 'price_prolong',
    'PE': 'price_change',

}


def registrator_list(request):
    if request.method == "POST":
        form = CompaniesSortForm(request.POST)
        if form.is_valid():
            sort_by = (form.cleaned_data['reverse_order']
                       + SORT_FIELD_NAMES.get(
                        form.cleaned_data['sort_by'], 'name'))
            search = form.cleaned_data['search']

    else:
        form = CompaniesSortForm()
        sort_by = 'id'
        search = ''

    if search:
        companies = Price.objects.filter(Q(registrator__name__icontains=search) | Q(
            registrator__city__icontains=search) | Q(price_reg__icontains=search))
    else:
        companies = Price.objects.filter()

    companies = companies.order_by('registrator_id', '-parse__id')
    companies = Price.objects.filter(id__in=companies).distinct('registrator_id')
    companies = Price.objects.filter(id__in=companies).order_by(sort_by)

    return render(request, 'registrator-list.html', {'companies': companies, 'form': form})


def registrator_details(request, id):
    try:
        registrator = Registrator.objects.get(id=id)
        prices = Price.objects.filter(registrator=registrator)
    except Price.DoesNotExist:
        return HttpResponseNotFound(f"Компания с идентификатором {id} в базе не найдена.")
    return render(request, 'registrator-details.html', {'prices': prices, 'registrator': registrator})


def about(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Логика обработки из формы обратной связи
            # отправка сообщения по почте админу.
            # TODO
            name = request.POST.get("name")
            contact = request.POST.get("contact")
            speciality = request.POST.get("speciality")
            message = request.POST.get("message")
            print(f"{name}\n{contact}\n{speciality}\n{message}")
    else:
        form = ContactForm()

    team_members = TeamMember.objects.all()

    return render(request, 'about-us.html', {'contact_form': form, 'team_members': team_members})


def project_view(request):
    return render(request, 'project.html')
