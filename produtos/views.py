from django.shortcuts import render
from django.http import HttpResponse

def ver_produto(request):
    nome = 'Carlos'
    return render(request, 'ver_produto.html', {'nome': nome})

def inserir_produto(request):
    return HttpResponse('Estou no inserir')