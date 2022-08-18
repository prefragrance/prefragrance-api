from django.contrib import admin
from search.models import UserProductSearch

@admin.register(UserProductSearch)
class UserProductSearchAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
    )

    ordering = (
        'pub_date',
    )
