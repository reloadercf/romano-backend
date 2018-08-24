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
from articulos import urls as articulos_urls
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from accounts import urls as perfiles_urls
from rest_framework import routers
from articulos.views import ArticuloViewSet,AleatoriaViewSet
############Rutas API
router = routers.DefaultRouter()
router.register('articulos', ArticuloViewSet)
router.register('publicidadrandom', AleatoriaViewSet)
############Path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(articulos_urls,namespace='articulo')),
    path('escritor/',include(perfiles_urls,namespace='escritor')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
    path('article/', include(router.urls)),
]
