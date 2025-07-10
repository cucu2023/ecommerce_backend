from .api import ProductoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/productos', ProductoViewSet, 'Productos')

urlpatterns = router.urls
