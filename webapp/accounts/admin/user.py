from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin View for User"""

    list_display = (
        "email",
        "username",
    )

    search_fields = (
        "email",
        "username",
    )

    ordering = (
        "username",
    )