from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin configuration for the username-free CustomUser model."""

    # Sort users alphabetically by email in the admin list view
    ordering = ("email",)
    
    # Sort users alphabetically by email in the admin list view
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )

    # Layout structure for the user detail/edit page split into sections
    fieldsets = (
        (None, {
            "fields": (
                "email",
                "password",
            )
        }),
        ("Personal info", {
            "fields": (
                "first_name",
                "last_name",
            )
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
    )