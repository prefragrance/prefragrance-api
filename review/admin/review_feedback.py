from django.contrib import admin
from review.models import ReviewFeedback


@admin.register(ReviewFeedback)
class ReviewFeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "review",
        "pub_date",
    )
    list_display_links = (
        "user",
    )
    search_fields = (
        "user",
    )
    ordering = (
        "pub_date",
    )
