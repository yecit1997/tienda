from django.urls import path
from .views import create_proveedor, list_proveedores

app_name = 'proveedores'

urlpatterns = [
    path('', list_proveedores.as_view(), name='listar_proveedores'),
    path('crear-proveedor/', create_proveedor.as_view(), name='crear_proveedor'),
]
