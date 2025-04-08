from django.shortcuts import render
from django.http import HttpResponse   

# Create your views here.

def home(request):
    return render(request, 'home.html')

def Cliente(request):
    context = {
        'nome': 'leonardo dias',
        'idade': 12,
        'cidade': 'São joaquim da barra'
    }
    return render(request, 'Cliente_Cadastro.html', context)

def Cliente_pedido(request): 
    context = {
        'cod_pedido': 1,
        'cod_item': 12
    }
    return render(request, 'Cliente_pedido.html', context)
     
