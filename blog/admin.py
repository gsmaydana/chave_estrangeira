from django.contrib import admin

from blog.forms import ContatoForm
from blog.models import *

# Register your models here.
admin.site.register(Autor)
admin.site.register(Tag)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("data_envio", "nome", "email", "telefone")
    search_fields = ("nome", "email", "mensagem")
    list_filter = ("data_envio",)
    
    form = ContatoForm
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "criado_em", "atualizado_em")
    search_fields = ("titulo", "subtitulo", "autor")
    list_filter = ("criado_em", "autor")
    