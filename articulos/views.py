from django.shortcuts import render
from django.views.generic import View
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .models import Articulo,Categoria,Aleatoria
from .serializers import ArticuloSerializer,AleatoriaSerializer,CategoriaSerializer
from rest_framework import viewsets, generics, filters
from rest_framework.filters import SearchFilter,OrderingFilter
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ArticuloView(View):
    def get(self, request):
        template_name = 'articulos/articulo_list.html'
        destacado=Articulo.objects.filter(destacado=True).order_by('id')
        object_list=Articulo.objects.all().order_by('-id')
        team=Categoria.objects.all()
        context={
            'object_list': object_list,
            'categoria': team,
            'destacados':destacado
        }
        return render(request, template_name, context)




class ArticuloDetalle(View):
    def get(self, request, slug):
        template_name='articulos/articulo_detail.html'
        query = Articulo.objects.get(slug=slug)
        team = Categoria.objects.all()
        context={
            'object':query,
            'categoria': team
        }
        return render(request, template_name, context)

#################APIS#############3
class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class AleatoriaViewSet(viewsets.ModelViewSet):
    queryset = Aleatoria.objects.all()
    serializer_class = AleatoriaSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ArticuloFiltro(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

    def get_queryset(self,*args,**kwargs):
        categoria = self.request.GET.get("q")
        revista =   self.request.GET.get("r")
        queryset_list = super(ArticuloFiltro, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria__nombrecategoria=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista__nombreregion=revista)
        return queryset_list
