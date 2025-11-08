from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ClienteForm, CustomUserCreationForm
from django.urls import reverse_lazy

from django.views import View
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'clientes/login.html'
    redirect_authenticated_user = True
    # Valor por defecto cuando no hay ?next=...: redirigir a registro (o cambia por la URL que quieras)
    success_url = reverse_lazy('clientes:register')

    def get_success_url(self):
        """
        Prioriza el parámetro `next` (en POST o GET). Si no existe, usa `success_url`.
        Esto permite que enlaces que incluyan `?next=/ruta/` funcionen correctamente.
        """
        # Django usa `redirect_field_name` (por defecto 'next') para buscar la URL de redirección
        redirect_to = self.request.POST.get(self.redirect_field_name) or self.request.GET.get(self.redirect_field_name)
        if redirect_to:
            return redirect_to
        return str(self.success_url)

    def form_valid(self, form):
        # Llama al método original para manejar el login (éste devolverá la redirección apropiada)
        response = super().form_valid(form)
        # Añade el mensaje de éxito
        messages.success(self.request, f"¡Bienvenido de nuevo, {self.request.user.username}!")
        return response
    
    
class CustomLogoutView(LogoutView):
    next_page = 'clientes:login'
    
    def dispatch(self, request, *args, **kwargs):
        # Agrega un mensaje antes de que el usuario sea desconectado
        messages.info(request, "Has cerrado sesión correctamente.")
        # Llama al método dispatch original para ejecutar el logout y la redirección
        return super().dispatch(request, *args, **kwargs)
    

class RegistroClienteView(View):
    template_name = 'clientes/registro.html' 
    
    def get(self, request):
        user_form = CustomUserCreationForm()
        cliente_form = ClienteForm()
        
        context = {
            'user_form': user_form,
            'cliente_form': cliente_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = CustomUserCreationForm(request.POST)
        cliente_form = ClienteForm(request.POST)

        if user_form.is_valid() and cliente_form.is_valid():
            
            # 1. Guardar el objeto User (esto maneja Nombre, Apellido, Usuario, Contraseña)
            new_user = user_form.save()
            
            # 2. Guardar el objeto Cliente (Teléfono, Dirección)
            cliente_perfil = cliente_form.save(commit=False)
            cliente_perfil.usuario = new_user
            cliente_perfil.save()
            
            # Opcional: Iniciar sesión al nuevo usuario
            # login(request, new_user)
            
            # Éxito: Redirigir a la página principal
            # return redirect('productos:inicio') 
            return redirect('clientes:login') # Redireccion de prueba

        # Fracaso: Volver a renderizar con errores
        context = {
            'user_form': user_form,
            'cliente_form': cliente_form,
        }
        return render(request, self.template_name, context)
