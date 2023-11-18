from django.db import models

class Salads(models.Model):
    Tipo = models.CharField(max_length=30)
    Sabor = models.CharField(max_length=30)
    Adic_ingre = models.CharField(max_length=250)
    Cantidad = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.Tipo} - {self.Sabor}'