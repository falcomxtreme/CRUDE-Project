# Generated by Django 5.0.1 on 2024-01-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tarefas', '0013_remove_tarefa_escolherordem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='Status',
            field=models.CharField(choices=[('Em Andamento', 'Em Andamento'), ('Pendente', 'Pendente'), ('Concluída', 'Concluída')], max_length=20),
        ),
    ]