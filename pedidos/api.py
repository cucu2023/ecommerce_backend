from rest_framework import viewsets, permissions
from .models import Pedido, DetallePedido
from .serializers import PedidoSerializer, DetallePedidoSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PedidoSerializer

    def perform_create(self, serializer):
        serializer.save(cliente=self.request.user)


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallePedidoSerializer

    def perform_create(self, serializer):
        serializer.save(pedido=self.request.data.get('pedido'),
                        precio_unitario=self.request.data.get('precio_unitario'))
