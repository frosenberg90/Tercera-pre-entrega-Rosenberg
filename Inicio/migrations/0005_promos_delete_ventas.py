# Generated by Django 4.2.6 on 2023-11-02 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0004_clientes_ventas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalmonLover', models.TextField()),
                ('MixAndTry', models.TextField()),
                ('CantidadS', models.IntegerField()),
                ('CantidadM', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Ventas',
        ),
    ]