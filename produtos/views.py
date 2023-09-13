from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_produto(request):
    if request.method == "GET":
        nome = 'Carlos'
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        pessoas = Pessoa.objects.filter(nome=nome)
        if pessoas.exists():
            HttpResponse("Usuário já cadastrado")
        else:
            HttpResponse("Usuário cadastrado")
        return HttpResponse("ok")


def inserir_produto(request):
    return HttpResponse('Estou no inserir')