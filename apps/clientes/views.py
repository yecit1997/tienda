from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ClienteForm, CustomUserCreationForm

from django.views import View
from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'clientes/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        # Llama al método original para manejar el login
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
    


def create_user(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('clientes:login')
    else:
        form = ClienteForm()
    
    return render(request, 'clientes/registro.html', {'form': form})


# clientes/views.py




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
            return redirect('clientes:login') 

        # Fracaso: Volver a renderizar con errores
        context = {
            'user_form': user_form,
            'cliente_form': cliente_form,
        }
        return render(request, self.template_name, context)
