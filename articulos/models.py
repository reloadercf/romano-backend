from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Categoria(models.Model):
    nombrecategoria     =models.CharField(max_length=200)
    def __str__(self):
        return self.nombrecategoria

class Region(models.Model):
    nombreregion        =models.CharField(max_length=200)
    def __str__(self):
        return self.nombreregion

class Articulo(models.Model):
    titulo              =models.CharField(max_length=150)
    textoprevio         =models.CharField(max_length=200)
    imagenportada       =models.ImageField(upload_to='media/')
    textograndecuerpo   =models.CharField(max_length=100)
    tipo                =models.CharField(max_length=100)
    cuerpo              =models.TextField()
    publicidad1         =models.ImageField(upload_to='media/')
    publicidad2         =models.ImageField(upload_to='media/')
    slug                =models.CharField(max_length=200, blank=True, null=True, unique=True)
    categoria           =models.ForeignKey(Categoria, related_name='category', on_delete=models.CASCADE)
    revista             =models.ForeignKey(Region, related_name='zona', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo


# Esta funcion genera un SLUG para cada perfil de usuario
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save_receiver, sender=Articulo)



# Esta funcion genera un SLUG para cada perfil de usuario
def pre_save_articulo(sender, instance, *args, **kwargs):
    if not instance.titulo:
        instance.titulo = '%s' % (instance.articulo.titulo)


pre_save.connect(pre_save_articulo, sender=Articulo)
