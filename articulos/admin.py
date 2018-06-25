from django.contrib import admin
from .models import Articulo,Region,Categoria

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Region)
admin.site.register(Categoria)