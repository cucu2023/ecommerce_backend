from .api import PedidoViewSet, DetallePedidoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'pedidos', PedidoViewSet, 'Pedidos')
router.register(r'detalle', DetallePedidoViewSet, 'DetallePedidos')
urlpatterns = router.urls
