from django.db import models

class Categoria(models.Model):

    tipo = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.tipo

class Adicionar(models.Model):

    nome = models.CharField(max_length=200)
    ano = models.DecimalField(max_digits=4, decimal_places=0)
    tipo = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default = 'Pendente')
 
    class Meta:
        verbose_name_plural = 'Adicionar'

    def __str__(self):

        return self.nome


# Create your models here.