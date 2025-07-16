from django.contrib import admin
from .models import Supplement, MealPlan
# Register your models here.


class SupplementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'price',
        'image',
    )


class MealPlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'calories',
        'price',
        'sku',
    )


admin.site.register(Supplement, SupplementAdmin)
admin.site.register(MealPlan, MealPlanAdmin)
