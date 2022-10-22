from django.contrib import admin
from product.models import Code

@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

    search_fields = (
        "name",
    )