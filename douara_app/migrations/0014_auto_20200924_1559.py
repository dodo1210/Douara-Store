# Generated by Django 3.1.1 on 2020-09-24 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('douara_app', '0013_oi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('frete', models.FloatField(blank=True, null=True)),
                ('quantidade', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='id',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='CEP2',
        ),
        migrations.AddField(
            model_name='produto',
            name='descrição',
            field=models.CharField(blank=True, max_length=60, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Oi',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='produto',
            field=models.ManyToManyField(to='douara_app.Produto'),
        ),
    ]