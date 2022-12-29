from django.urls import include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Demo Project for Goals API",
        default_version='v1',
        description="Demo Project for Goals API",
    ),
    public=True,
    authentication_classes=[JWTAuthentication],
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/', include('demo_django.urls')),
    path('drf/', include('demo_drf.urls')),
    re_path(
        r"^drf/docs/swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path('__debug__/', include('debug_toolbar.urls')),
]
