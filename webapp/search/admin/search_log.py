from django.contrib import admin
from search.models import SearchLog

@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):

    list_display = (
        'content',
        'pub_date',
    )
