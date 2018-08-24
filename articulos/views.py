from django.shortcuts import render
from django.views.generic import View
from .models import Articulo,Categoria,Aleatoria
from .serializers import ArticuloSerializer,AleatoriaSerializer,CategoriaSerializer
from rest_framework import viewsets
from django.db.models import Q
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
    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get()
        queryset_list = super(ArticuloFiltro, self).get_queryset()
        if search:
            queryset_list = queryset_list.filter(
                Q(categoria__icontains=search)
            ).distinct()

        return queryset_list