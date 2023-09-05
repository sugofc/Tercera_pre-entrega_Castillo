# Generated by Django 4.2.4 on 2023-09-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=11)),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('anio', models.IntegerField(verbose_name='Año')),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]