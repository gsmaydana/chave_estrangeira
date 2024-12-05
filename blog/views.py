from django.contrib import messages
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView

from blog.forms import ContatoForm
from blog.models import *

# Create your views here.
class PostListView(ListView):
    
    model = Post
    template_name = 'post_list.html'
    
    paginate_by = 10    
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        if self.request.GET.get('autor'):
            autor = self.request.GET.get('autor')
            qs = qs.filter(autor__nome=autor)
        
        if self.request.GET.get('tag'):
            tag = self.request.GET.get('tag')
            qs = qs.filter(tags__nome=tag)
            
        return qs
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        has_filters = bool(self.request.GET.get('autor') or self.request.GET.get('tag'))
        context['has_filters'] = has_filters
        context['current_filters'] = self.request.GET.dict()
        
        context['tags'] = Tag.objects.annotate(num_posts=Count('posts'))
        context['autores'] = Autor.objects.annotate(num_posts=Count('posts'))
        context['posts'] = self.get_queryset()
        
        return context
    
    
class PostDetailView(DetailView):
    
    model = Post
    template_name = 'post_detalhe.html'
        
    
class ContatoFormView(FormView):
    
    template_name = "contato.html"
    form_class = ContatoForm
    success_url = reverse_lazy("contato")


    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Sua mensagem foi enviada com sucesso!")
        return super().form_valid(form)