# from django.db import models
# import uuid

# from apps.proveedores.models import Proveedor

# class Producto(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nombre = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     precio = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')
#     imagen = models.ImageField(upload_to='productos/', default='static/assets/default.png', null=True, blank=True)
#     creado_en = models.DateTimeField(auto_now_add=True)
#     actualizado_en = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nombre
    
#     class Meta:
#         verbose_name = "Producto"
#         verbose_name_plural = "Productos"
#         ordering = ['-creado_en']
