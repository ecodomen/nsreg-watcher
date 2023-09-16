from django.db import models


class Registrator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    nic_handle1 = models.TextField()
    nic_handle2 = models.TextField()
    website = models.TextField()
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'regcomp'

    def __str__(self):
        return f'{self.id}: {self.name}'

    @staticmethod
    def get_registrator(id):
        return Registrator.objects.get(id=id)


class Domain(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'domain'

    def __str__(self):
        return self.name


class ParseHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'parse_history'

    def __str__(self):
        return str(self.date)


class Price(models.Model):
    id = models.BigAutoField(primary_key=True)
    registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    parse = models.ForeignKey(ParseHistory, on_delete=models.CASCADE)
    price_reg = models.DecimalField(max_digits=10, decimal_places=2)
    price_prolong = models.DecimalField(max_digits=10, decimal_places=2)
    price_change = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'price'

    def __str__(self):
        return f'{self.id}: {self.price_reg}, {self.price_prolong}, {self.price_change}'


class Parser(models.Model):
    id = models.BigAutoField(primary_key=True)
    registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming the use of Django's default user model
    contributor_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'parser'

    def __str__(self):
        return f'{self.id}: {self.contributor_name}'


class ParseError(models.Model):
    id = models.BigAutoField(primary_key=True)
    parse = models.ForeignKey(ParseHistory, on_delete=models.CASCADE)
    parser = models.ForeignKey(Parser, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        managed = False
        db_table = 'parse_error'

    def __str__(self):
        return f'{self.id}: {self.message}'
