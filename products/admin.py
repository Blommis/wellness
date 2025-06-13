from django.contrib import admin
from .models import Supplement
# Register your models here.

class SupplementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'image',
    )


admin.site.register(Supplement, SupplementAdmin)
