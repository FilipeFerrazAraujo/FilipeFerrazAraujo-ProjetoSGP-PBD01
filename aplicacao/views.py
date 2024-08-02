from django.shortcuts import render, get_object_or_404, redirect
from .models import Veiculo, Abastecimento
from .forms import VeiculoForm, AbastecimentoForm
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
  return render(request, 'index.html')

def get_veiculos(request):
  veiculos = Veiculo.objects.order_by('placa')
  context = {'veiculos':veiculos}
  return render(request, 'veiculo/veiculos.html', context)

def get_veiculo(request, id):
  veiculo = get_object_or_404(Veiculo, pk=id)
  context = {'veiculo':veiculo}
  return render(request, 'veiculo/veiculo.html', context)

def add_veiculo(request):
  if request.method != 'POST':
    form = VeiculoForm()
  else:
    form = VeiculoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('veiculos')
  context = {'form':form}
  return render(request, 'veiculo/add_veiculo.html', context) 

def up_veiculo(request, id):
  veiculo = get_object_or_404(Veiculo, pk= id)
  if request.method != 'POST':
    form = VeiculoForm(instance=veiculo)
  else:
    form = VeiculoForm(request.POST, instance=veiculo)
    if form.is_valid():
      form.save()
      return redirect('veiculo', id= veiculo.id)
  context = {'form':form}
  return render(request, 'veiculo/up_veiculo.html', context)

def delete_veiculo(request, id):
  veiculo = get_object_or_404(Veiculo, pk= id)
  if request.method == 'POST':
    veiculo.delete()
    return redirect('veiculos')
  context = {'veiculo':veiculo}
  return render(request, 'veiculo/delete_veiculo.html', context)

def get_abastecimentos(request):
  abas = Abastecimento.objects.order_by('-data_abastecimento')
  context = {'abas':abas}
  return render(request,'abastecimento/abas.html', context)

def get_abastecimento(request, id):
  aba = get_object_or_404(Abastecimento, pk= id)
  context = {'aba':aba}
  return render(request, 'abastecimento/aba.html', context)

def add_abastecimento(request):
  if request.method != 'POST':
    form = AbastecimentoForm()
  else:
    form = AbastecimentoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('abas')
  return render(request, 'abastecimento/add_aba.html', {'form':form})

def delete_abastecimento(request, id):
  aba = get_object_or_404(Abastecimento, pk=id)
  if request.method == 'POST':
    aba.delete()
    return redirect('abas')
  return render(request, 'abastecimento/del_aba.html', {'aba':aba})
  
def up_abastecimento(request, id):
  abastecimento = get_object_or_404(Abastecimento, pk= id)
  if request.method != 'POST':
    form = AbastecimentoForm(instance=abastecimento)
  else:
    form = AbastecimentoForm(request.POST, instance=abastecimento)
    if form.is_valid():
      form.save()
      return redirect('aba', id= abastecimento.id)
  return render(request, 'abastecimento/up_aba.html', {'form':form})