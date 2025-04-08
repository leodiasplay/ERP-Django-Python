from django.contrib import admin   
from django.urls import include, path   
from .views import Cliente, Cliente_pedido, home  
from django.views.generic import TemplateView
from . import views
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cadastro/', Cliente, name='cliente_cadastro'),
    path('pedidos/', Cliente_pedido, name='cliente_pedidos'),
    
    path('', TemplateView.as_view(template_name='navbar.html'), name='navbar'),
]