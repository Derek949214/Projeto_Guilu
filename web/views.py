from django.shortcuts import render, redirect
from .models import Adicionar
from .form import AdicionarForm
from datetime import datetime
import requests, json


def user(request):

    data = dict()
    data['adicionados'] = ['Buscar Filmes e Séries', 'Ver Lista de Desejos']

    data['now'] = datetime.now()

    return render(request, 'web/user.html', data)

def busca(request):

    search = request.GET.get('search')
    tipo = request.GET.get('tipo').lower()

    model = Adicionar
  
    if tipo == 'filme':

        tipo = 'movie'

    elif tipo == 'série':

        tipo = 'series'

    response1 = requests.get("http://www.omdbapi.com/?apikey=7db9f6c4&s={}&type={}&plot=full".format(search, tipo)).json()
    
    # for tamanho in range(0, len(response1['Search'])):

    #     model.nome = response1['Search'][tamanho]['Title']
    #     model.ano = response1['Search'][tamanho]['Year']
    #     model.tipo = response1['Search'][tamanho]['Type']

    if response1['Response'] == 'False':

        response = requests.get("http://www.omdbapi.com/?apikey=7db9f6c4&t={}&type={}&plot=full".format(search, tipo)).json()

        # for tamanho in range(0, len(response1['Search'])):

        #     model.nome = response['Title']
        #     model.ano = response['Year']
        #     model.tipo = response['Type']

        if response['Response'] == 'False':

            response = requests.get("http://www.omdbapi.com/?apikey=7db9f6c4&t={}&type={}&plot=full".format(search, tipo)).json()
            
            return render(request, 'web/busca.html', response)

        else:

            return render(request, 'web/busca.html', response)

    else:

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
