# Generated by Django 3.1.1 on 2020-10-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('douara_app', '0017_auto_20200924_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
