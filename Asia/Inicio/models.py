from django.db import models

# Create your models here.
class Productos(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    costo = models.IntegerField()
    cantidad = models.IntegerField()

        
        
    def __str__(self):
        return f'{self.id}-{self.tipo}-{self.descripcion}-{self.cantidad}'

class ventas(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    costo = models.IntegerField()
    cantidad = models.IntegerField()

        
        
    def __str__(self):
        return f'{self.id}-{self.tipo}-{self.descripcion}-{self.cantidad}'

class Clientes(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    costo = models.IntegerField()
    cantidad = models.IntegerField()

        
        
    def __str__(self):
        return f'{self.id}-{self.tipo}-{self.descripcion}-{self.cantidad}'
