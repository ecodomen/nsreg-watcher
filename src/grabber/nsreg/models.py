import django
import os
from django.db import models
from django.conf import settings as django_settings

from .settings import DEFAULT_SETTINGS

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

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
