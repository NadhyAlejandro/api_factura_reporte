from rest_framework import serializers
from api.models import Cliente, Tipo_cliente

class TipoClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Tipo_cliente
        fields = "__all__"

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"
