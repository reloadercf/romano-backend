from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo              =models.CharField(max_length=150)
    textoprevio         =models.CharField(max_length=200)
    imagenportada       =models.ImageField(upload_to='media/')
    textograndecuerpo   =models.CharField(max_length=100)
    tipo                =models.CharField(max_length=100)
    cuerpo              =models.TextField()
    publicidad1         =models.ImageField(upload_to='media/')
    publicidad2         =models.ImageField(upload_to='media/')
    def __str__(self):
        return self.titulo
    
    