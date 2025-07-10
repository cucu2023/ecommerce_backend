from .api import CategoriaViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api/categorias', CategoriaViewSet, 'categorias')

urlpatterns = router.urls
