from django.shortcuts import render
from django.http import HttpResponse  

# Create your views here.

def cliente(request):
    nome = 'leonardo dias'
    idade = 12
    cidade = 'São joaquim da barra'
    return render(request, 'Cliente_Cadastro.html')
