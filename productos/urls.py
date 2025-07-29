from .api import DetalleProductoViewSet, ProductoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet, 'Productos')
router.register(r'detalle_producto',
                DetalleProductoViewSet, 'Detalle_Producto')
urlpatterns = router.urls
