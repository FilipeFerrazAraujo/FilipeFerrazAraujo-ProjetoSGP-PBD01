from django.db import models

# Create your models here.
class Veiculo(models.Model):
  
  class Combustivel(models.TextChoices):
    GASOLINA = 'gasolina'
    DIESEL = 'diesel'
    
  modelo = models.CharField(max_length=200)
  marca = models.CharField(max_length=200)
  placa = models.CharField(max_length=11, unique=True)
  combustivel = models.CharField(max_length=8, choices= Combustivel.choices)
  ano_lancamento = models.IntegerField()
  
  def __str__(self):
    return self.placa
  
class Abastecimento(models.Model):
  
  class Tipo(models.TextChoices):
    GASOLINA = 'gasolina'
    DIESEL = 'diesel'
  
  veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
  tipo = models.CharField(max_length=8, choices=Tipo.choices)
  total_litros = models.IntegerField()
  valor_litro = models.DecimalField(max_digits=4, decimal_places=2)
  data_abastecimento = models.DateTimeField(unique=True)
  
  
  @property
  def valor_total(self):
    return self.valor_litro * self.total_litros
  
  def __str__(self) -> str:
    return f'{self.data_abastecimento}'