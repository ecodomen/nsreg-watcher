from django.urls import path
from whois_lookup import views

urlpatterns = [
    path('', views.domain_lookup, name='domain_lookup'),
]
