from django.contrib import admin
from review.models import Review, ReviewFeedback

class LikeInline(admin.StackedInline):
    model = ReviewFeedback

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    inlines = (
        LikeInline,
    )

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
