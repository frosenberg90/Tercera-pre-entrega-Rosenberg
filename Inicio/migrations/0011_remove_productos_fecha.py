# Generated by Django 4.2.6 on 2023-11-18 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0010_alter_productos_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='fecha',
        ),
    ]
