from django.contrib import admin
from products.models import Categories

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass
