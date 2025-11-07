# from django.db import models
# import uuid

# class Proveedor(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nombre = models.CharField(max_length=100)
#     direccion = models.CharField(max_length=255)
#     telefono = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     creado_en = models.DateTimeField(auto_now_add=True)
#     actualizado_en = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.nombre
    
#     class Meta:
#         verbose_name = "Proveedor"
#         verbose_name_plural = "Proveedores"
#         ordering = ['-creado_en']