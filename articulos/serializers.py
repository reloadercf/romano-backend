from rest_framework import serializers
from .models import Articulo,Aleatoria,Categoria,Region
from accounts.models import Perfil

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields='__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields='__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Perfil
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    autor=PerfilSerializer(many=False,read_only=True)
    categoria=CategoriaSerializer(many=False,read_only=True)
    revista=RegionSerializer(many=False,read_only=True)
    class Meta:
        model=Articulo
        fields = '__all__'

class AleatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aleatoria
        fields = '__all__'
