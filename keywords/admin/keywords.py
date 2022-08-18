from django.contrib import admin
from keywords.models import Keywords

@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    pass
