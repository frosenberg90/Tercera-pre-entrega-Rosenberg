# Generated by Django 4.2.6 on 2023-11-18 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0009_alter_productos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
