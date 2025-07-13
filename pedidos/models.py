from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
# Create your models here.
ESTADOS_PEDIDO = (
    ('pendiente', 'Pendiente'),
    ('enviado', 'Enviado'),
    ('entregado', 'Entregado'),
    ('cancelado', 'Cancelado'),
)


class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS_PEDIDO,
        default='pendiente'
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    direccion_envio = models.CharField(max_length=255, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=15, blank=True, null=True)


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
