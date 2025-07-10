from rest_framework import serializers
from .models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion',
                  'fecha_actualizacion', 'slug', 'imagen']
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion', 'slug']
