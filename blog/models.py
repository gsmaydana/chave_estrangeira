from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.

class Autor(models.Model):
    
    nome = models.CharField(max_length=100, verbose_name="Nome")
    
    email = models.EmailField(verbose_name="E-mail")
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.nome} ({self.email})"
    
    
class Tag(models.Model):
    
    nome = models.CharField(max_length=255, verbose_name='Nome', blank=False, null=False)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nome
    
    
class Post(models.Model):
    
    is_destaque = models.BooleanField(default=False, verbose_name="Destaque?")
    
    titulo = models.CharField(max_length=1000, null=False)
    
    subtitulo = models.CharField(max_length=1000, null=False)
    
    texto = models.TextField(null=False)
    
    imagem = models.FileField(upload_to='img/posts/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, null=False, blank=False, related_name='posts')
    
    tags = models.ManyToManyField(Tag, related_name='posts')

    criado_em = models.DateTimeField(auto_now_add=True)
    
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-criado_em']
        
    def __str__(self):
        return self.titulo


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
