from django.urls import path
from .views import Usuario_cadastro, Usuario_permicoes 

urlpatterns = [
    # Defina as URLs do seu app aqui
    path('cadastro/', Usuario_cadastro, name='Usuario_cadastro'),
    path('permicoes/', Usuario_permicoes, name='Usuario_permicoes',)
]