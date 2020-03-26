from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def user(request):
    now = datetime.now()

    return render(request, 'web/user.html')

# Create your views here.
