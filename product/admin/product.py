from django.contrib import admin
from product.models import Product, ProductFeedback
from review.models import Review
import random

def copy_product(self, request, queryset):
    string_pool = "abcdef"

    for product in queryset:
        random_string = random.choice(string_pool)
        product.pk = None
        product.name = product.name + random_string
        product.save()


copy_product.short_description = "상품을 복사합니다."

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
    actions = (
        copy_product,
    )