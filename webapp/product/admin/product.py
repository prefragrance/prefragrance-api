import random

from django.contrib import admin

from product.models import Product, ProductFeedback
from review.models import Review


def copy_product(self, request, queryset):
    string_pool = "abcdefghijklmnopqrstuvwxyz"

    for product in queryset:
        random_string = random.choice(string_pool)
        product.pk = None
        product.name = product.name + random_string
        product.producer = product.producer + random_string
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
        "tag_list",
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
    actions = (copy_product,)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
