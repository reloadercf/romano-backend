"""mxasturiasbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from rest_framework import routers
from articulos.views import ArticuloViewSet,AleatoriaViewSet,CategoriasViewSet,ArticuloFiltro
from directorio.views import DirectorioViewset
from django.views.generic import TemplateView

class inicio(TemplateView):
    template_name = 'index.html'

############Rutas API
router = routers.DefaultRouter()
router.register('articulos', ArticuloViewSet)
router.register('publicidadrandom', AleatoriaViewSet)
router.register('categorias',CategoriasViewSet)
router.register('articulofiltro',ArticuloFiltro)
router.register('directorio',DirectorioViewset)
############Path
urlpatterns = [
    path('',inicio.as_view(),name='index'),
    path('publicar/', admin.site.urls),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
    path('article/', include(router.urls)),
]