from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Proveedor
from .proveedores_forms import ProveedorForm


class create_proveedor(CreateView):
    template_name = "proveedores/crear_proveedor.html"
    form_class = ProveedorForm
    success_url = reverse_lazy("proveedores:listar_proveedores")


class list_proveedores(ListView):
    template_name = "proveedores/lista_proveedor.html"
    model = Proveedor
    context_object_name = "proveedores"
