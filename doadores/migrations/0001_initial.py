# Generated by Django 3.0.8 on 2020-07-07 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('tipo_sanguineo', models.CharField(max_length=2)),
                ('fator_rh', models.BooleanField()),
            ],
        ),
    ]
