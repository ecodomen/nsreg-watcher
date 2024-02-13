from .models import Price, Registrator, ParseHistory
from rest_framework import serializers


class RegistratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrator
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    registrator = RegistratorSerializer(read_only=True)
    parse = serializers.PrimaryKeyRelatedField(queryset=ParseHistory.objects.all())

    class Meta:
        model = Price
        fields = "__all__"
