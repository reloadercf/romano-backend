from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Articulo
# Create your views here.
class ArticuloView(ListView):
    model = Articulo

class ArticuloDetalle(View):
    def get(self, request, slug):
        template_name='articulos/articulo_detail.html'
        query = Articulo.objects.get(slug=slug)
        context={
            'object':query,
        }
        return render(request, template_name, context)