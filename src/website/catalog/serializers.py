from .models import Price, Registrator
from rest_framework import serializers


class RegistratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrator
        fields = "__all__"
    # id
    # name
    # nic_handle1
    # nic_hanlde2
    # website
    # city


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fileds = "__all__"
    # id = models.BigAutoField(primary_key=True)
    # registrator = models.ForeignKey(Registrator, on_delete=models.CASCADE)
    # domain = models.CharField("Домен", max_length=10, choices=DOMAINS)
    # parse = models.ForeignKey(ParseHistory, on_delete=models.CASCADE, null=True)
    # price_reg = models.DecimalField("Регистрация", max_digits=10, decimal_places=2)
    # price_prolong = models.DecimalField("Продление", max_digits=10, decimal_places=2)
    # price_change = models.DecimalField("Перенос", max_digits=10, decimal_places=2)
    # created_at = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    # updated_at = models.DateTimeField("Дата изменения", auto_now=True, null=True)
    # reg_status = models.CharField("Статус", max_length=1, choices=VALID_CHOICES, default="V")
    # prolong_status = models.CharField("Статус", max_length=1, choices=VALID_CHOICES, default="V")
    # change_status = models.CharField("Статус", max_length=1, choices=VALID_CHOICES, default="V")