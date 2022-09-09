from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from accounts.models import User


# # Register your models here.
class UserAdmin(UserAdmin):
    class Meta:
        Model = User

    list_display = [
        "name",
        "email",
        "is_staff",
        "is_active",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    list_per_page = 10
    fieldsets = (
        (None, {"fields": ("name", "email", "password")}),
        ("permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)
