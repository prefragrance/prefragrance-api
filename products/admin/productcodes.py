from django.contrib import admin
from products.models import ProductCodes

@admin.register(ProductCodes)
class ProductCodesAdmin(admin.ModelAdmin):
    pass
