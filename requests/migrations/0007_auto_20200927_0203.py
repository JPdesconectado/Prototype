# Generated by Django 3.1 on 2020-09-27 05:03

import cpf_field.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_auto_20200927_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitacaoeducacao',
            name='cadastro_pf',
            field=cpf_field.models.CPFField(default=0, max_length=14, verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitacaoeducacao',
            name='comentario',
            field=models.TextField(default=(0,)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitacaoeducacao',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='solicitacaoeducacao',
            name='rg',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]