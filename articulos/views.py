from .models import Articulo,Categoria,Aleatoria
from .serializers import ArticuloSerializer,AleatoriaSerializer,CategoriaSerializer
from rest_framework import viewsets
from .pagination import ArticlePagination
# Create your views here.


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
    pagination_class = ArticlePagination

    def get_queryset(self,*args,**kwargs):
        categoria = self.request.GET.get("q")
        revista =   self.request.GET.get("r")
        titulo=     self.request.GET.get("slug")
        queryset_list = super(ArticuloFiltro, self).get_queryset()
        if categoria:
            queryset_list = queryset_list.filter(categoria__nombrecategoria=categoria)
        if revista:
            queryset_list = queryset_list.filter(revista__nombreregion=revista)
        if titulo:
            queryset_list = queryset_list.filter(slug=titulo)
        return queryset_list