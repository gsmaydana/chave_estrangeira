from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from blog.forms import ContatoForm
from blog.models import *

# Create your views here.
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    
    
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detalhe.html'
    
    
class ContatoFormView(FormView):
    template_name = "contato.html"
    form_class = ContatoForm
    success_url = reverse_lazy("contato")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Sua mensagem foi enviada com sucesso!")
        return super().form_valid(form)