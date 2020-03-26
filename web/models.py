from django.db import models

class Categoria(models.Model):

    tipo = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)


# Create your models here.