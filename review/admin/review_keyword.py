from django.contrib import admin
from review.models import ReviewKeyword


@admin.register(ReviewKeyword)
class ReviewKeywordAdmin(admin.ModelAdmin):

    list_display = (
        "review_id",
        "keyword_id",
    )
    list_display_links = (
        "review_id",
    )
    readonly_fields = (
        "review_id",
    )
    search_fields = (
        "keyword_id",
    )
    ordering = (
        "id",
    )
