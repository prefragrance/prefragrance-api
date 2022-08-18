from django.contrib import admin
from products.models import ProductKeyword

@admin.register(ProductKeyword)

class ProductKeywordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "keyword_id",
    )

    search_fields = list_display