from django.shortcuts import render

def Usuario_cadastro(request): 
    context = {
        'cod_usuario': 1
    }
    return render(request, 'Usuario_cadastro.html', context)

def Usuario_permicoes(request): 
    context = {
        'cod_permisao': 1
    }
    return render(request, 'Usuario_permicoes.html', context)