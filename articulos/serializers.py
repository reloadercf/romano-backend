from rest_framework import serializers
from .models import Articulo,Aleatoria

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articulo
        fields = '__all__'

class AleatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aleatoria
        fields = '__all__'