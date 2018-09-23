from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from accounts.models import Perfil

# Create your models here.
class Categoria(models.Model):
    nombrecategoria     =models.CharField(max_length=200)
    def __str__(self):
        return self.nombrecategoria

class Planesvigentes(models.Model):
    plan=models.CharField(max_length=50)
    caracteristicas=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.plan

class Region(models.Model):
    nombreregion        =models.CharField(max_length=200)
    Usuarios            =models.ManyToManyField(User)
    portada             =models.ImageField(upload_to='revistas/', blank=True, null=True)
    def __str__(self):
        return self.nombreregion

class Cliente(models.Model):
    nombre_patrocinador =models.CharField(max_length=100)
    razonsocial         =models.CharField(max_length=200)
    correo              =models.EmailField(null=True,blank=True)
    telefono            =models.IntegerField(null=True,blank=True)
    numero_cuenta       =models.IntegerField(null=True,blank=True)
    zona                =models.ManyToManyField(Region)
    fechacontrato       =models.DateField()
    terminocontrato     =models.DateField()
    plan_contratado     =models.ForeignKey(Planesvigentes, related_name='tipoplan',on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_patrocinador

tiposdearticulos=(
    ('patrocinado','patrocinado'),
    ('prueba','prueba'),
    ('corporativo','corporativo'),
    ('institucional','institucional'),
    ('estrategico','estrategico'),
)
botones=(
    ('Llamar','Llamar'),
    ('Visitar','Visitar'),
    ('Comprar','Comprar'),
)
posiciones=(
                ('arriba','arriba'),
                ('abajo','abajo'),
                ('sinvideo','sinvideo'),
            )
class Articulo(models.Model):
    destacado           =models.BooleanField(default=False)
    titulo              =models.CharField(max_length=150)
    textoprevio         =models.CharField(max_length=200)
    imagenportada       =models.ImageField(upload_to='media/')
    textograndecuerpo   =models.CharField(max_length=100)
    tipo                =models.CharField(choices=tiposdearticulos,default='patrocinado',max_length=50)
    cuerpo              =models.TextField()
    publicidad1         =models.ImageField(upload_to='media/')
    numero_llamada1     =models.CharField(max_length=20,blank=True,null=True)
    link1               =models.URLField(null=True,blank=True)
    boton1              =models.CharField(choices=botones,default='Visitar',max_length=10)
    publicidad2         =models.ImageField(upload_to='media/')
    numero_llamada2     =models.CharField(max_length=20, blank=True, null=True)
    link2               =models.URLField(null=True,blank=True)
    boton2              =models.CharField(choices=botones, default='Visitar', max_length=10)
    slug                =models.CharField(max_length=200, blank=True, null=True, unique=True)
    categoria           =models.ForeignKey(Categoria, related_name='category', on_delete=models.CASCADE)
    revista             =models.ForeignKey(Region, related_name='zona', on_delete=models.CASCADE)
    fechainicio         =models.DateField(auto_now_add=True)
    fechafin            =models.DateField()
    autor               =models.ForeignKey(Perfil,related_name='escritor', on_delete=models.CASCADE)
    linkvideo           =models.URLField(null=True,blank=True)
    posicionvideo       =models.CharField(choices=posiciones,default='sinvideo',max_length=15)
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

class Aleatoria(models.Model):
    imagen= models.ImageField(upload_to='media/aleatoria',blank=True,null=True)
    descripcion=models.CharField(max_length=100,blank=True,null=True)

