# Generated by Django 4.2.6 on 2023-11-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0007_rename_cantidadm_promos_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]