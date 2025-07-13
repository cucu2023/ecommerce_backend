from .api import ProductoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet, 'Productos')

urlpatterns = router.urls
