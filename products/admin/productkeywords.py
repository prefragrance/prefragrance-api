from django.contrib import admin
from products.models import ProductKeywords

@admin.register(ProductKeywords)
class ProductKeywordsAdmin(admin.ModelAdmin):
    pass
