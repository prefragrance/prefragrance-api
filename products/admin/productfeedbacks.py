from django.contrib import admin
from products.models import ProductFeedbacks

@admin.register(ProductFeedbacks)
class ProductFeedbacksAdmin(admin.ModelAdmin):
    pass
