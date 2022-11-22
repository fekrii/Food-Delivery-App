from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Food Delivery App",
        default_version='1.0.0',
        description="API documentation of Food Delivery App",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('_auth.urls')),
    path('api/', include('core.urls')),

    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema"),
    
]
