from django.db import models


class Registrator(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Наименование", max_length=255)
    nic_handle1 = models.TextField()
    nic_handle2 = models.TextField()
    website = models.TextField("Сайт")
    city = models.CharField("Город", max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'

    @staticmethod
    def get_registrator(id):
        return Registrator.objects.get(id=id)

    class Meta:
        verbose_name = 'Регистратор'
        verbose_name_plural = 'Регистраторы'
        app_label = 'catalog'


# class Domain(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    name = models.CharField(max_length=255)
#
#    def __str__(self):
#        return self.name


class ParseHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField("Дата парсинга", auto_now=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        app_label = 'catalog'


class Price(models.Model):
    DOMAINS = [
            ("ru", "Ru"),
    ]
    id = models.BigAutoField(primary_key=True)
    registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    domain = models.CharField("Домен", max_length=10, choices=DOMAINS)
    parse = models.ForeignKey(ParseHistory, on_delete=models.CASCADE, null=True)
    price_reg = models.DecimalField("Регистрация", max_digits=10, decimal_places=2, blank=True, null=True)
    price_prolong = models.DecimalField("Продление", max_digits=10, decimal_places=2, blank=True, null=True)
    price_change = models.DecimalField("Перенос", max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Дата изменения", auto_now=True, null=True)

    def __str__(self):
        return f'{self.id}: {self.price_reg}, {self.price_prolong}, {self.price_change}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
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
