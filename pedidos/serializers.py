from rest_framework import serializers
from .models import Pedido, DetallePedido


class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        read_only_fields = ['fecha_pedido', 'total']


class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'
        read_only_fields = ['pedido', 'precio_unitario']
