from articulos.models import Region
from articulos.models import Cliente
from .models import Categoriadirectorio,Directorio
from rest_framework import serializers

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields='__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields='__all__'
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoriadirectorio
        fields='__all__'

class DirectorioSerializer(serializers.ModelSerializer):
    zona=ZonaSerializer(many=False,read_only=True)
    cliente=ClienteSerializer(many=False,read_only=True)
    categori=CategoriaSerializer(many=False,read_only=True)
    class Meta:
        model=Directorio
        fields='__all__'