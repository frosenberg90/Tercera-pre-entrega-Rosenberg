# Generated by Django 4.2.6 on 2023-11-18 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cuentas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosextra',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
