from django.contrib import admin
from product.models import ProductFeedback

@admin.register(ProductFeedback)
class ProductFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "user",
    )

    search_fields = list_display