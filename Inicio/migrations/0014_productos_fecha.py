# Generated by Django 4.2.6 on 2023-11-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0013_remove_productos_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
