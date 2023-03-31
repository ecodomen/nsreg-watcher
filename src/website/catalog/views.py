from django.shortcuts import render
from django.http import HttpResponse
from .models import Regcomp


def regcomp_list(request):
    companies = Regcomp.company_list()
    return render(request, 'regcomp-list.html', {'companies': companies})
