from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['telefono', 'direccion']

        # Opcional: Personalizar etiquetas
        labels = {
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
        }
        
        # Opcional: Personalizar widgets (ej. clases CSS para el input)
        widgets = {
            'telefono': forms.TextInput(attrs={'placeholder': 'Ej: 555-1234'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ej: Calle Falsa 123'}),
        }
        
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class CustomLoginForm(AuthenticationForm):
    # Sobrescribimos 'username' y 'password' que ya están en AuthenticationForm
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre de usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )
    
    
    