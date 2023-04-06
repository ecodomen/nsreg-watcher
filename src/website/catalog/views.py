from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Regcomp


def regcomp_list(request):
    companies = Regcomp.objects.all()
    return render(request, 'regcomp-list.html', {'companies': companies})

def regcomp_details(request, id):
    try:
        company = Regcomp.objects.get(id=id)
    except Regcomp.DoesNotExist:
        return HttpResponseNotFound(f"Компания с идентификатором {id} в базе не найдена.")         
    return render(request, 'regcomp-details.html', {'company': company})

def about(request):
    return render(request, 'about-us.html', )

