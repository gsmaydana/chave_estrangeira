from django.db.models import Count
from django.shortcuts import render

from blog.models import Autor, Tag, Post


def index(request):
    
    destaque = Post.objects.filter(is_destaque=True).first()
    posts = Post.objects.filter(is_destaque=False).order_by('-criado_em')[:5]
    tags = Tag.objects.annotate(num_posts=Count('posts'))
    autores = Autor.objects.annotate(num_posts=Count('posts'))

    return render(request, 'index.html', locals())
    
    
def sobre(request):
    
    return render(request, 'sobre.html', {})