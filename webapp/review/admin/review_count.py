from django.contrib import admin
from review.models import ReviewCount


@admin.register(ReviewCount)
class ReviewFeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "gold_medal",
        "silver_medal",
        "bronze_medal"
    )

