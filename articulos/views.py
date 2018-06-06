from django.shortcuts import render
from django.views.generic import ListView
from .models import Articulo
# Create your views here.
class ArticuloView(ListView):
    model = Articulo