from rest_framework import serializers
from .models import Producto, ImagenProducto


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = ['id', 'imagen']


class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = [
            'id', 'nombre', 'descripcion', 'precio_regular', 'categoria',
            'precio_promocional', 'estado', 'talla', 'color',
            'cantidad_disponible', 'fecha_creacion', 'fecha_actualizacion',
            'imagenes'
        ]
        read_only_fields = ['fecha_creacion', 'fecha_actualizacion']
