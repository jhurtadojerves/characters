"""Register all models in admin"""

from django.contrib import admin

# Local
from .models import Award, Category, AccessToken, Voting
from characters.models import Character


class AwardAdmin(admin.ModelAdmin):
    """Config Admin from Award Model"""

    list_display = ["name", "description", "slug"]


class CategoryAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "id",
        "name",
        "description",
        "award",
        "status",
        "max_options",
        "order",
        "self_voting",
        "slug",
    )
    list_editable = (
        "name",
        "status",
        "max_options",
        "self_voting",
        "order",
        "description",
    )
    filter_horizontal = ("participants",)


class AccessTokenAdmin(admin.ModelAdmin):
    """Config access token model"""

    list_display = ["token", "user", "character", "get_url"]


admin.site.register(Award, AwardAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Voting)
