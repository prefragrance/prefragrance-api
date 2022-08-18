from django.contrib import admin
from products.models import ProductFeedback

@admin.register(ProductFeedback)
class ProductFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product_id",
        "user_id",
    )

    search_fields = list_display