from django.contrib import admin
from .models import Articulo,Region,Categoria,Cliente,Planesvigentes

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Region)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Planesvigentes)
