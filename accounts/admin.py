from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username", "first_name", "last_name", "email",
        "phone", "is_active", "last_login",
    )
    fieldsets = UserAdmin.fieldsets + (("Extra details", {"fields": ("phone",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Extra details", {"fields": ("phone",)}),
    )