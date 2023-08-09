import datetime
from django.db import models


class Registrator(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)
    note1 = models.TextField(blank=False, null=False)
    note2 = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    website = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'registrator'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def get_registrator(id):
        Registrator.objects.get(id=id)

class Domain(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'domain'

    def __str__(self):
        return f'{self.id}: {self.name}'

class Parse_History(models.Model):
    date = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'parse_history'

class Parser(models.Model):
    id_registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    contributor_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'parser'

class Price(models.Model):
    id_registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    id_domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    id_parse_history = models.ForeignKey(Parse_History, on_delete=models.CASCADE)
    registration_price = models.FloatField(blank=True, null=True)
    prolongation_price = models.FloatField(blank=True, null=True)
    changing_price = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'price'

class Parse_Error(models.Model):
    id_parse_history = models.ForeignKey(Parse_History, on_delete=models.CASCADE)
    id_parser = models.ForeignKey(Parser, on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'parse_error'