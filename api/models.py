from django.db import models
class Tipo_cliente (models.Model):
    tipo = models.CharField(max_length=80)  

class Cliente (models.Model):
    nombre = models.CharField(max_length=80)
    cedula = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    monto_primera_compra = models.FloatField()
    tipo=models.ForeignKey(Tipo_cliente,on_delete=models.PROTECT)
# otros modelos...
