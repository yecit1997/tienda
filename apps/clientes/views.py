from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'clientes/login.html'
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    next_page = 'clientes:login'
    

