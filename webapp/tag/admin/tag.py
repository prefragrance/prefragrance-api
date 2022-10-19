from django.contrib import admin
from tag.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin VIEW for Tag"""
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