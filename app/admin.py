from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    Award,
    AwardTransaction,
    Challenge,
    ChallengeItem,
    ChallengeTransaction,
)

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Define the fields to be used in displaying the User model.
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (_("Points"), {"fields": ("point_earned",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "point_earned",
                ),
            },
        ),
    )

    # Extend the list_display to include custom fields
    list_display = (
        "username",
        "point_earned",
    )

    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(AwardTransaction)
class AwardTransactionAdmin(admin.ModelAdmin):
    list_display = ("award", "user", "created_at")
    list_filter = ("created_at", "award")
    search_fields = ("user__username", "award__name")


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "point", "award")
    search_fields = ("title", "description")
    list_filter = ("award",)


@admin.register(ChallengeItem)
class ChallengeItemAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "challenge")
    search_fields = ("title", "description")
    list_filter = ("challenge",)


@admin.register(ChallengeTransaction)
class ChallengeTransactionAdmin(admin.ModelAdmin):
    list_display = ("challenge_item", "user", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at", "challenge_item")
    search_fields = ("user__username", "challenge_item__title")
