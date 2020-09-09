# Generated by Django 3.1 on 2020-09-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0004_auto_20200909_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='referencia',
            new_name='complemento',
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='status',
            name='atual',
            field=models.CharField(choices=[('Recebido', 'Recebido'), ('Em andamento', 'Em andamento'), ('Recusado', 'Recusado'), ('Concluído', 'Concluído')], default='Recebido', max_length=100),
        ),
    ]