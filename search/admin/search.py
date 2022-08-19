from django.contrib import admin
from search.models import Search

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'cnt',
    )
