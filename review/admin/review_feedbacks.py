from django.contrib import admin
from review.models import ReviewFeedback


@admin.register(ReviewFeedback)
class ReviewFeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "user_id",
        "review_id",
        "pub_date",
    )
    list_display_links = (
        "user_id",
    )
    readonly_fields = (
        "pub_date",
    )
    search_fields = (
        "user_id",
    )
    ordering = (
        "pub_date",
    )
