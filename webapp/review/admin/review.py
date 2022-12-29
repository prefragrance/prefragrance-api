from django.contrib import admin

from accounts.models import User
from product.models import Product
from review.models import Review, ReviewFeedback


class LikeInline(admin.StackedInline):
    model = ReviewFeedback

def copy_review(self, request, queryset):
    review = queryset[0]

    for product in Product.objects.all():
        review.pk = None
        review.product = product
        review.save()


copy_review.short_description = "리뷰를 복사합니다."

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    inlines = (LikeInline,)

    list_display = (
        "user",
        "product",
        "content",
        "pub_date",
        "tag_list",
    )
    list_display_links = ("user",)
    search_fields = ("product",)
    ordering = ("pub_date",)
    actions = (copy_review,)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
