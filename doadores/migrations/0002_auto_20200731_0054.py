# Generated by Django 3.0.8 on 2020-07-31 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doador',
            name='fator_rh',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
