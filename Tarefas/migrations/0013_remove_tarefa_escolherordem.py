# Generated by Django 5.0.1 on 2024-01-05 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefas', '0012_tarefa_escolherordem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='EscolherOrdem',
        ),
    ]
