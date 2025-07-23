from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Producto, ImagenProducto
from .serializers import ProductoSerializer, ImagenSerializer

# Listar todos los productos y crear uno nuevo


class ProductoListCreateView(APIView):
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Obtener, actualizar o eliminar un producto por id


class ProductoDetailView(APIView):
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(
            producto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ImagenProductoListCreateView(APIView):
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        imagenes = ImagenProducto.objects.filter(producto=producto)
        serializer = ImagenSerializer(imagenes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
