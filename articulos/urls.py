from django.urls import path
from .views import ArticuloView

app_name='articulos'

urlpatterns=[
    path('',ArticuloView.as_view(),name='articulos'),
]