# Generated by Django 4.2.6 on 2023-11-18 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0015_alter_productos_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='descripcion',
        ),
    ]
