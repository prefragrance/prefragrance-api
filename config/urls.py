from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="prefragrance",
        default_version="v1",
        description="API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="prefragrance@gmail.com"),
        license=openapi.License(name="MIT LICENSE"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        r"?P<format>\.json|\.yaml",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        '',
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        r"redoc", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc-v1"
    ),
    path('api/accounts/', include('accounts.urls')),
    path("api/search/",include('search.urls')),
    path("api/product/", include('product.urls')),
    path("api/review/", include('review.urls')),
]
