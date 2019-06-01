from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['id', 'center_id', 'name', 'email', 'nick_name', 'phone',
                    'is_partner', 'created_datetime', 'updated_datetime']
    list_display_links = ['id', 'name']
