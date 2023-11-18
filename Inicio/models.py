from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Productos(models.Model):
    tipo = models.CharField(max_length=30)
    descripcion =RichTextField(null=True)
    costo = models.IntegerField()
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now=True)
        
        
    def __str__(self):
        return f'{self.id}-{self.tipo}-{self.cantidad}-{self.fecha}'

class Promos(models.Model):

    Promo = models.CharField(max_length=30)
    Cantidad = models.IntegerField()
    
        
        
    def __str__(self):
        return f'{self.Promo}-{self.Cantidad}'

class Clientes(models.Model):
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Edad=models.IntegerField()
    genero=models.CharField(max_length=2)      
        
    def __str__(self):
        return f'{self.id}-{self.Apellido}-{self.genero}'
    
