from django.contrib import admin
from review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "product",
        "content",
        "pub_date",
    )
    list_display_links = (
        "user",
    )
    search_fields = (
        "product",
    )
    ordering = (
        "pub_date",
    )
