from django.contrib import admin
from review.models import ReviewTag


@admin.register(ReviewTag)
class ReviewTagAdmin(admin.ModelAdmin):

    list_display = (
        "review_id",
        "tag_id",
    )
    list_display_links = (
        "review_id",
    )
    search_fields = (
        "tag_id",
    )
    ordering = (
        "id",
    )
