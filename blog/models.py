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