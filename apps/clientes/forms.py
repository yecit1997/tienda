# clientes/forms.py

from django import forms
from .models import Cliente
from django.contrib.auth.models import User

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
        
class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }