from django.contrib import admin
from keywords.models import Keyword

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    """Admin VIEW for Keyword"""
    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "id",
    )