from django.forms import models
from .models import Veiculo, Abastecimento

class VeiculoForm(models.ModelForm):
  
  class Meta:
    model = Veiculo
    fields = ['modelo', 'marca', 'placa', 'combustivel', 'ano_lancamento']
    
    
class AbastecimentoForm(models.ModelForm):
  
  class Meta:
    model = Abastecimento
    fields = ['veiculo', 'tipo','total_litros','valor_litro', 'data_abastecimento']
    