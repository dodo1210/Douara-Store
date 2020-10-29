# Generated by Django 3.1.1 on 2020-09-24 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('douara_app', '0006_auto_20200922_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('frete', models.FloatField(blank=True, null=True)),
                ('produto', models.ManyToManyField(to='douara_app.Produto')),
            ],
        ),
    ]