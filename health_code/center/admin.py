from django.contrib import admin

from .models import Center, CenterCategory, Program, Membership


@admin.register(CenterCategory)
class CenterCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_datetime', 'updated_datetime']
    list_display_links = ['id', 'name']


@admin.register(Center)
class CenterModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'phone', 'address', 'longitude', 'latitude', 'is_active',
                    'description', 'created_datetime', 'updated_datetime']
    list_display_links = ['id', 'name']


@admin.register(Program)
class ProgramModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'center', 'name', 'quota', 'price', 'available', 'program_schedule', 'description',
                    'is_active', 'created_datetime', 'updated_datetime']
    list_display_links = ['id', 'name']


@admin.register(Membership)
class MembershipModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'center_id', 'program_id', 'start_date', 'end_date',
                    'created_datetime', 'updated_datetime']