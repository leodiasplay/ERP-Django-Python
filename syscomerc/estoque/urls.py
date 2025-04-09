from django.urls import path
from .views import Cadastro_item 

urlpatterns = [
    # Defina as URLs do seu app aqui
    path('Cadastro_item/', Cadastro_item, name='Cadastro_item'),
    
]