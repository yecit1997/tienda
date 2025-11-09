from django.urls import path
from .views import CustomLoginView, CustomLogoutView, RegistroClienteView

app_name = 'clientes'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegistroClienteView.as_view(), name='register'),
]

