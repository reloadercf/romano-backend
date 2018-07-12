from django.shortcuts import render
from .models import Perfil
from django.views.generic import View
# Create your views here.

class PerfilDetalle(View):
    def get(self, request, slug):
        template_name='accounts/perfil_detail.html'
        query = Perfil.objects.get(slug=slug)
        context={
            'object':query,
        }
        return render(request, template_name, context)