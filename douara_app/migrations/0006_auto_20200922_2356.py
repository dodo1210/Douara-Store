# Generated by Django 3.1.1 on 2020-09-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douara_app', '0005_produto_imagem_hover'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='CEP',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='CPF_CNPJ',
            field=models.CharField(blank=True, max_length=18),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='complemento',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='numero',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='rua',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
