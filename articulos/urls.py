from django.urls import path
from .views import ArticuloView,ArticuloDetalle

app_name='articulos'

urlpatterns=[
    path('',ArticuloView.as_view(),name='articulos'),
    path('articulo/<slug:slug>/', ArticuloDetalle.as_view(), name='articulocompleto'),
]