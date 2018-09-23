from django.db import models
from articulos.models import Region
from articulos.models import Cliente
# Create your models here.

class Categoriadirectorio (models.Model):
    categoria=models.CharField( max_length=250,blank=True,null=True)
    def __str__(self):
        return self.categoria


    #logotipo ubicacion fotografia de lugar descripcion
class Directorio (models.Model):
    nombre_publico=models.CharField(max_length=300)
    categori=models.ForeignKey(Categoriadirectorio,related_name='catego',on_delete=models.CASCADE)
    palabras_clave=models.CharField(max_length=500,blank=True,null=True)
    zona=models.ForeignKey(Region,related_name='localidad',on_delete=models.CASCADE)
    direccion=models.CharField(max_length=500)
    cliente=models.ForeignKey(Cliente,related_name='contratante',on_delete=models.CASCADE)
    ubicacion=models.URLField(blank=True,null=True)
    telefono=models.CharField(max_length=20,null=True,blank=True)
    telefonodos = models.CharField(max_length=20,null=True,blank=True)
    correo=models.EmailField(null=True,blank=True)
    sitioweb=models.URLField(blank=True,null=True)
    logotipo=models.ImageField(blank=True,null=True,upload_to='directorio/logos')
    imagen1=models.ImageField(blank=True,null=True, upload_to='directorio/fotos')
    imagen2 = models.ImageField(blank=True, null=True, upload_to='directorio/fotos')
    descripcion=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.nombre_publico