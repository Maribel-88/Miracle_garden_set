from django.contrib import admin
from .models import Gardenset, Category

# Register your models here.

class GardensetAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'basic_name',
        'name',
    )


admin.site.register(Gardenset,GardensetAdmin)
admin.site.register(Category, CategoryAdmin)