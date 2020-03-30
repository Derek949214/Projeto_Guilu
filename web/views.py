from django.shortcuts import render, redirect
from .models import Adicionar
from .form import AdicionarForm
from datetime import datetime
import requests, json


def user(request):

    data = dict()
    data['adicionados'] = ['Buscar Filmes e Séries', 'Ver Lista de Desejos', 'Alterar Status', 'Remover Conteúdo da Lista de Desejos']

    data['now'] = datetime.now()

    return render(request, 'web/user.html', data)

def busca(request):

    # pesquisa = AdicionarForm(request.POST or None)

    response1 = requests.get("http://www.omdbapi.com/?apikey=7db9f6c4&s=matrix&type=movie&plot=full").json()

    return render(request, 'web/busca.html', response1)

def lista_de_desejos(request):

    data = dict()

    data['adicionados'] = Adicionar.objects.all()
    return render(request, 'web/desejo.html', data)

def novo_adicionamento(request):

    data = dict()

    form = AdicionarForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('url_desejo')

    data['form'] = form

    return render(request, 'web/form.html', data)

def update(request, pk):

    data = dict()

    adicionar = Adicionar.objects.get(pk=pk)
    form = AdicionarForm(request.POST or None, instance=adicionar)

    if form.is_valid():

        form.save()

        return redirect('url_user')

    data['form'] = form
    data['adicionar'] = adicionar

    return render(request, 'web/form.html', data)

def delete(request, pk):

    adicionar = Adicionar.objects.get(pk=pk)
    adicionar.delete()

    return redirect('url_desejo')

# Create your views here.
