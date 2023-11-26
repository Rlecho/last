# Importez les modules nécessaires
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configurez les schémas Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Gestion de Métriques API",
        default_version='v1',
        description="API pour la gestion de métriques IoT",
        # terms_of_service="https://www.example.com/terms/",
        terms_of_service="http://127.0.0.1:8000/",
        contact=openapi.Contact(email="elechoserge@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentification.urls')),
    path('api/', include('utilisateurs.urls')),
    path('api/', include('compteurs_electriques.urls')),
    path('api/', include('facturation.urls')),
    path('api/', include('recharges.urls')),
    path('api/', include('proprietes.urls')),
    path('', include('gestionnaires.urls')),

    # Définition des schémas Swagger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
