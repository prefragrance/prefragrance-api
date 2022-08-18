from django.contrib import admin
from search.models import UserSearch

@admin.register(UserSearch)
class UserSearchAdmin(admin.ModelAdmin):
    list_display = (
            'user',
            'product',
        )

    ordering = (
        'pub_date',
    )
