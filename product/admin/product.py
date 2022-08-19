from django.contrib import admin
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "name",
        "producer",
        "feedback_cnt",
        "review_cnt",
        "visit_cnt",
        "rate_sum",
        "rate",
    )

    list_display_links = list_display

    search_fields = (
        "name",
        "producer",
        "category",
    )