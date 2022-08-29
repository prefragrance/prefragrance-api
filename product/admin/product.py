from django.contrib import admin
from product.models import Product, ProductFeedback
from review.models import Review



class ReviewInline(admin.StackedInline):
    model = Review

class LikeInline(admin.StackedInline):
    model = ProductFeedback

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
    inlines = (
        ReviewInline,
        LikeInline,
    )
    list_display_links = list_display

    search_fields = (
        "name",
        "producer",
        "category",
    )