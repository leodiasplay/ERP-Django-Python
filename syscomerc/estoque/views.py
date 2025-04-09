from django.shortcuts import render

# Create your views here.

def Cadastro_item(request): 
    context = {
        'cod_item': 1
    }
    return render(request, 'Cadastro_item.html', context)
