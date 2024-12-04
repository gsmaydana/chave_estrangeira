from django.db.models import Count
from django.shortcuts import render

from blog.models import Categoria, Post


def index(request):
    
    posts = Post.objects.all().order_by('-criado_em')[:5]
    destaque = Post.objects.filter(is_destaque=True).first()
    
    categorias = Categoria.objects.annotate(num_posts=Count('posts'))

    return render(request, 'index.html', locals())
    
    
def sobre(request):
    
    return render(request, 'sobre.html', {})