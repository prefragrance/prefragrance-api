from django.contrib import admin
from search.models import RecommendSearch

@admin.register(RecommendSearch)
class RecommendSearchAdmin(admin.ModelAdmin):
    list_display = (
        'content',
    )
