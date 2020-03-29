from django.forms import ModelForm
from .models import Adicionar

class AdicionarForm(ModelForm):

    class Meta:

        model = Adicionar
        fields = ['nome', 'ano', 'tipo', 'status']