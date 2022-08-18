from django.contrib import admin
from products.models import Codes

@admin.register(Codes)
class CodesAdmin(admin.ModelAdmin):
    pass
