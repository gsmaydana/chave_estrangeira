from django.utils import timezone

from blog.models import Categoria


def get_data_formatada(data):
    fuso_horario = timezone.get_current_timezone()
    data_hora_formatada = timezone.localtime(
        data, fuso_horario).strftime('%d/%m/%Y %H:%M:%S')
    return data_hora_formatada


def chave_estrangeira_context_processor(request):
    
    contexto = dict(
        categorias = Categoria.objects.all()
    )

    return contexto
