from rest_framework import viewsets, permissions
from .models import Producto, DetalleProducto
from .serializers import ProductoSerializer, DetalleProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer


class DetalleProductoViewSet(viewsets.ModelViewSet):
    queryset = DetalleProducto.objects.all()
    serializer_class = DetalleProductoSerializer
