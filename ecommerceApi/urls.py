from django.contrib import admin
from django.urls import include, path
from django.utils.module_loading import cached_import
from docutils.nodes import description
from pygments.lexer import default
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Mi API",
        default_version='v1',
        description="Documentacion de la api"
    ),
    public=True,
    permission_classes=(permissions.AllowAny),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/productos/', include('productos.urls')),
    path('api/categorias/', include('categoria.urls')),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
