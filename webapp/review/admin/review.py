from django.contrib import admin

from review.models import Review, ReviewFeedback


class LikeInline(admin.StackedInline):
    model = ReviewFeedback


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

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return ", ".join(o.name for o in obj.tags.all())
