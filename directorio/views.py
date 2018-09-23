from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DirectorioSerializer
from .models import Directorio
# Create your views here.

class DirectorioViewset(viewsets.ModelViewSet):
    queryset = Directorio.objects.all()
    serializer_class = DirectorioSerializer
    def get_queryset(self,*args,**kwargs):
        categori = self.request.GET.get("categoria")
        zona =   self.request.GET.get("revista")
        nombre_publico=     self.request.GET.get("name")
        palabras_clave=self.request.GET.get("palabras")
        queryset_list = super(DirectorioViewset, self).get_queryset()
        if categori:
            queryset_list = queryset_list.filter(categori__categoria=categori)
        if zona:
            queryset_list = queryset_list.filter(zona__nombreregion=zona)
        if nombre_publico:
            queryset_list = queryset_list.filter(nombre_publico=nombre_publico)
        if palabras_clave:
            queryset_list=queryset_list.filter(palabras_clave=palabras_clave)
        return queryset_list