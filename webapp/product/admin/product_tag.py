from django.contrib import admin
from product.models import ProductTag

@admin.register(ProductTag)

class ProductTagAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "tag",
    )

    search_fields = list_display