import django
import os
from django.db import models
from django.conf import settings as django_settings

from .settings import DEFAULT_SETTINGS

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

if not django_settings.configured:
    django_settings.configure(**DEFAULT_SETTINGS)
    django.setup()


class Registrator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nic_handle1 = models.TextField()
    nic_handle2 = models.TextField()
    website = models.TextField()
    city = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'

    @staticmethod
    def get_registrator(id):
        return Registrator.objects.get(id=id)

    class Meta:
        app_label = 'catalog'


# class Domain(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    name = models.CharField(max_length=255)
#
#    def __str__(self):
#        return self.name


class ParseHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        app_label = 'catalog'


class Price(models.Model):
    DOMAINS = [
        ('ru', 'Ru'),
    ]
    VALID_CHOICES = [
        ('V', 'valid'),
        ('A', 'absent'),
    ]
    id = models.BigAutoField(primary_key=True)
    registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    domain = models.CharField(max_length=10, choices=DOMAINS)
    parse = models.ForeignKey(ParseHistory, on_delete=models.CASCADE)
    price_reg = models.DecimalField(max_digits=10, decimal_places=2)
    price_prolong = models.DecimalField(max_digits=10, decimal_places=2)
    price_change = models.DecimalField(max_digits=10, decimal_places=2)
    reg_status = models.CharField('Статус', max_length=1, choices=VALID_CHOICES, default='V')
    prolong_status = models.CharField('Статус', max_length=1, choices=VALID_CHOICES, default='V')
    change_status = models.CharField('Статус', max_length=1, choices=VALID_CHOICES, default='V')

    def __str__(self):
        return f'{self.id}: {self.price_reg}, {self.price_prolong}, {self.price_change}'

    class Meta:
        app_label = 'catalog'


class Parser(models.Model):
    id = models.BigAutoField(primary_key=True)
    registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming the use of Django's default user model
    contributor_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.contributor_name}'

    class Meta:
        app_label = 'catalog'


class ParseError(models.Model):
    id = models.BigAutoField(primary_key=True)
    parse = models.ForeignKey(ParseHistory, on_delete=models.CASCADE)
    parser = models.ForeignKey(Parser, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.message}'

    class Meta:
        app_label = 'catalog'
