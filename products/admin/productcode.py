from django.contrib import admin
from products.models import ProductCode
from ..models.product import Product

@admin.register(ProductCode)
class ProductCodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "code_id",
    )

    search_fields = list_display