"""Register all models in admin"""

# Django
from django.contrib import admin

# Local
from .models import Achievement, Point, Road


class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "road",
        "points",
        "get_icon_principal",
        "get_icon_secondary",
    )


class PointAdmin(admin.ModelAdmin):
    list_display = ("quantity", "character", "road", "reason", "creation_date")
    autocomplete_fields = ("character", "road")


class RoadAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Road, RoadAdmin)
