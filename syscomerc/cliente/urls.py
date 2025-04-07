from django.contrib import admin  
from django.urls import include, path  
from .views import cliente  
from django.views.generic import TemplateView  # <- Importação correta

urlpatterns = [
    path('cliente/', cliente),  # Adicione barra no final (boas práticas)
    path('', TemplateView.as_view(template_name='navbar.html'), name='navbar'),
]
