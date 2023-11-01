from django.db import models

# Create your models here.
class Productos(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion = models.TextField()
    costo = models.IntegerField()
    cantidad = models.IntegerField()

        
        
    def __str__(self):
        return f'{self.id}-{self.tipo}-{self.descripcion}-{self.cantidad}'

class Ventas(models.Model):
    producto = models.CharField(max_length=30)
    cantidad = models.IntegerField()

        
        
    def __str__(self):
        return f'{self.id}-{self.producto}-{self.cantidad}'

class Clientes(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Edad=models.IntegerField()
    genero=models.CharField()      
        
    def __str__(self):
        return f'{self.id}-{self.Apellido}-{self.genero}'
