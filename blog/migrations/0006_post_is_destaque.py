# Generated by Django 5.1.3 on 2024-12-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_categoria_options_remove_categoria_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_destaque',
            field=models.BooleanField(default=False, verbose_name='Destaque?'),
        ),
    ]