from django.contrib import admin

from chatroom import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ordering', 'slug']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name', 'category_type', 'fee_status', 'is_active',
        'created_at', 'updated_at'
    ]
    list_filter = ['category_type', 'fee_status', 'is_active']
    search_fields = ['name']


@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'category', 'name', 'is_active', 'created_at', 'updated_at'
    ]
    list_filter = ['category', 'is_active']
    search_fields = ['name']
