from django.contrib import admin
from product.models import ProductCode
from ..models.product import Product

@admin.register(ProductCode)
class ProductCodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "code",
    )

    search_fields = list_display