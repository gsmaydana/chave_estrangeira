# Generated by Django 5.1.3 on 2024-12-04 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_imagem'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Tag',
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['nome'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='categorias',
            new_name='tags',
        ),
    ]
