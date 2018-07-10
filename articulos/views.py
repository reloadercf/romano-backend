from django.shortcuts import render
from django.views.generic import View
from .models import Articulo,Categoria
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