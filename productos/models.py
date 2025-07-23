from django.db import models
from django.core.validators import MinValueValidator
from categoria.models import Categoria
from django.core.exceptions import ValidationError
# Create your models here.

ESTADO_CHOICES = [('Nuevo', 'Nuevo'),
                  ('Usado', 'Usado'),
                  ('Reacondicionado', 'Reacondicionado')]


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class DetalleProducto(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='variantes')
    talla = models.CharField(max_length=10, blank=True,
                             null=True, db_index=True)
    color = models.CharField(max_length=30, blank=True,
                             null=True, db_index=True)
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default='Nuevo', db_index=True)
    precio_regular = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)], default=0.01
    )
    precio_promocional = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0.01)], default=0.01
    )
    cantidad_disponible = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - {self.color} - {self.talla}"

    def clean(self):
        if self.precio_promocional > self.precio_regular:
            raise ValidationError(
                "El precio promocional no puede ser mayor que el precio regular.")


class ImagenProducto(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/')

    def __str__(self):
        return f"Imagen de {self.producto.nombre}"
