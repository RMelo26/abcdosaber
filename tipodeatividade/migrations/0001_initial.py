# Generated by Django 4.2.18 on 2025-02-25 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeAtividade',
            fields=[
                ('codigo', models.AutoField(help_text='Código do Tipo de Atividade', primary_key=True, serialize=False)),
                ('descricao', models.CharField(help_text='Informe a descrição do Tipo de Atividade', max_length=100)),
            ],
        ),
    ]
