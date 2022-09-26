from django.contrib import admin

from accounts.models import Visit


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Admin View for Visit"""

    list_display = (
        "user",
        "product",
        "pub_date",
    )

    ordering = ("pub_date",)
