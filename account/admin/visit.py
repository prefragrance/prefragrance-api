from django.contrib import admin
from account.models import Visit

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    """Admin View for Visit"""

    list_display = (
        "user",
        "product",
    )

    ordering = (
        "pub_date",
    )