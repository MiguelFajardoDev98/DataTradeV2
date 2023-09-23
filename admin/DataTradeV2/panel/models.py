from django.db import models

# Create your models here.

class Inventario(models.Model):
    codProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=100, null=False)
    valorUnidad = models.DecimalField(max_digits=30, decimal_places=2, null=False)
    cantidadProducto = models.IntegerField(null=False)
    fechaRegistro = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        db_table = 'tbInventario'