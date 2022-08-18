from django.contrib import admin
from review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user_id",
        "product_id",
        "content",
        "pub_date",
    )
    list_display_links = (
        "user_id",
    )
    search_fields = (
        "product_id",
    )
    ordering = (
        "pub_date",
    )
