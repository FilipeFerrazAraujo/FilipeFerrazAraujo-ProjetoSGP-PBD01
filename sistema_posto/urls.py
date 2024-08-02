"""
URL configuration for sistema_posto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacao.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name= 'index'),
    
    path('veiculos/', get_veiculos, name='veiculos'),
    path('veiculos/<int:id>', get_veiculo, name='veiculo'),
    path('veiculos/add', add_veiculo, name='add_veiculo'),
    path('veiculos/update/<int:id>', up_veiculo, name='up_veiculo'),
    path('veiculos/delete/<int:id>', delete_veiculo, name='del_veiculo'),
    
    path('abastecimentos/', get_abastecimentos, name='abas'),
    path('abastecimentos/<int:id>', get_abastecimento, name='aba'),
    path('abastecimentos/add', add_abastecimento, name='add_aba'),
    path('abastecimentos/update/<int:id>', up_abastecimento, name='up_aba'),
    path('abastecimentos/delete/<int:id>', delete_abastecimento, name='del_aba')
    
    
]
