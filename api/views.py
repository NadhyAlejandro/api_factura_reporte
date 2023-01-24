from rest_framework import viewsets
from api.models import Cliente,Tipo_cliente
from api.serializers import ClienteSerializer,TipoClienteSerializer

class TipoClienteViewSet ( viewsets.ModelViewSet ):
    serializer_class = TipoClienteSerializer
    queryset = Tipo_cliente.objects.all()
   
class ClienteViewSet ( viewsets.ModelViewSet ):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
