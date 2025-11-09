from django.urls import reverse_lazy
from .models import Producto
from . productos_forms import ProductoForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class ProductoListView(ListView):
    template_name = "productos/lista_productos.html"
    # Aquí iría el modelo Producto cuando esté definido
    model = Producto
    context_object_name = "productos"
    
class ProductoDetailView(CreateView):
    template_name = "productos/detalle_producto.html"
    # Aquí iría el modelo Producto cuando esté definido
    # model = Producto
    context_object_name = "producto"

class ProductoCreateView(CreateView):
    template_name = "productos/crear_producto.html"
    # Aquí iría el modelo Producto cuando esté definido
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy("productos:lista_productos")
    # fields = ['nombre', 'descripcion', 'precio', 'stock']
 
class ProductoUpdateView(UpdateView):
    template_name = "productos/actualizar_producto.html"
    # Aquí iría el modelo Producto cuando esté definido
    # model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'stock']

class ProductoDeleteView(DeleteView):
    template_name = "productos/eliminar_producto.html"
    # Aquí iría el modelo Producto cuando esté definido
    # model = Producto
    context_object_name = "producto"
