from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.db.models import Q

from hitcount.views import HitCountDetailView

from .models import Price, ParseHistory, Registrator
from .forms import CompaniesSortForm


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
            sort_by = SORT_FIELD_NAMES.get(
                form.cleaned_data['sort_by'], 'name')
            search = form.cleaned_data['search']
            companies = Price.objects.order_by(sort_by)

    else:
        form = CompaniesSortForm()
        sort_by = 'id'
        search = ''

    if search:
        companies = Price.objects.filter(Q(registrator__name__icontains=search) | Q(
            registrator__city__icontains=search) | Q(price_reg__icontains=search)).order_by(sort_by)
    else:
        last_parse = ParseHistory.objects.order_by("-id").all()[0]
        companies = list(Price.objects.filter(parse=last_parse).all().order_by(sort_by))
    return render(request, 'registrator-list.html', {'companies': companies, 'form': form})


class DetailRegistratorView(HitCountDetailView):
    model = Registrator
    template_name = 'registrator-details.html'
    context_object_name = 'company'
    count_hit = True

    def get_object(self, *args, **kwargs):
        id = self.kwargs.get('id')
        try:
            company = Registrator.objects.get(id=id)
        except Registrator.DoesNotExist:
            return HttpResponseNotFound(f"Компания с идентификатором {id} в базе не найдена.")
        return company

def about(request):
    return render(request, 'about-us.html', )


def project_view(request):
    return render(request, 'project.html')
