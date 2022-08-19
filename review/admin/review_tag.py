from django.contrib import admin
from review.models import ReviewTag


@admin.register(ReviewTag)
class ReviewTagAdmin(admin.ModelAdmin):

    list_display = (
        "review",
        "tag",
    )
    list_display_links = (
        "review",
    )
    search_fields = (
        "tag",
    )
    ordering = (
        "id",
    )
