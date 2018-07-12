from django.urls import path
from.views import PerfilDetalle

app_name='accounts'

urlpatterns = [
path('<slug:slug>/', PerfilDetalle.as_view(), name="autor"),
]