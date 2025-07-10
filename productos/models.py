from django.db import models
from django.core.validators import MinValueValidator
from categoria.models import Categoria
# Create your models here.

ESTADO_CHOICES = [('Nuevo', 'Nuevo'),
                  ('Usado', 'Usado'),
                  ('Reacondicionado', 'Reacondicionado')]


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_regular = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(0.01)], default=0.01)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio_promocional = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], default=0.01)
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='Nuevo')
    talla = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    cantidad_disponible = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/')
