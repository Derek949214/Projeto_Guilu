from django.shortcuts import render, redirect
from .models import Adicionar
from .form import AdicionarForm
from datetime import datetime


def user(request):

    data = dict()
    data['adicionados'] = ['Adicionar', 'Ver Lista de Desejos', 'Alterar Status', 'Remover Conteúdo da Lista de Desejos']
    data['adicionados'].append( Adicionar.objects.all())

    data['now'] = datetime.now()

    if data['adicionados'] == 'Alterar Status':

        return redirect('url_update')

    return render(request, 'web/user.html', data)

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
