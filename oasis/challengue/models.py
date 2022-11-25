from django.db import models

# Create your models here.

class deportista(models.Model):
    Nombre_apellidos = models.CharField(max_length=40)  
    Genero = models.CharField(max_length=40)
    Categoria= models.CharField(max_length=40,null=True)
    Puntos = models.IntegerField(null=True)
    
    def __str__(self):
        return self.Nombre_apellidos

class wod(models.Model):
    Deportista = models.ForeignKey(deportista,null=True,blank=True,on_delete=models.CASCADE)
    Wod_numero = models.IntegerField(null=True)
    Puntos = models.IntegerField(null=True)