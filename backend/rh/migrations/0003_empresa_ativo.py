# Generated by Django 2.2.4 on 2019-08-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rh', '0002_auto_20190805_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
