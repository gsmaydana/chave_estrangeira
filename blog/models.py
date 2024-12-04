from django.db import models

# Create your models here.
class Categoria(models.Model):
    
    nome = models.CharField(max_length=255, verbose_name='Nome', blank=False, null=False)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome
    

class Contato(models.Model):
    
    nome = models.CharField(max_length=100, verbose_name="Nome")
    
    email = models.EmailField(verbose_name="E-mail")
    
    telefone = models.CharField(max_length=15, verbose_name="Telefone", blank=True, null=True)
    
    mensagem = models.TextField(verbose_name="Mensagem")
    
    data_envio = models.DateTimeField(auto_now_add=True, verbose_name="Data de Envio")

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
        ordering = ["-data_envio"]

    def __str__(self):
        return f"{self.nome} ({self.email})"
