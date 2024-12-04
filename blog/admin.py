from django.contrib import admin

from blog.forms import ContatoForm
from blog.models import *

# Register your models here.
admin.site.register(Categoria)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ("data_envio", "nome", "email", "telefone")
    search_fields = ("nome", "email", "mensagem")
    list_filter = ("data_envio",)
    
    form = ContatoForm