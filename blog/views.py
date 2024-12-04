from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import *

# Create your views here.
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    
    
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detalhe.html'