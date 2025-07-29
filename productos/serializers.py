from rest_framework import serializers
from .models import Producto, ImagenProducto, DetalleProducto


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenProducto
        fields = ['id', 'imagen']


class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        exclude = ['fecha_creacion', 'fecha_actualizacion']


class DetalleProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleProducto
        fields = '__all__'
        # Nombres de los campos a excluir
