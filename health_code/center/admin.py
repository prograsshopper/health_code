from django.contrib import admin

from .models import Center, CenterCategory


@admin.register(CenterCategory)
class CenterCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_datetime', 'updated_datetime']
    list_display_links = ['id', 'name']


@admin.register(Center)
class CenterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'phone', 'address', 'longitude', 'latitude', 'is_active', 'description', 'created_datetime', 'updated_datetime']
    list_display_links = ['id', 'name']
