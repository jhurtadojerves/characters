"""Register all models in admin"""

# Django
from django.contrib import admin

# Local
from .models import Achievement, Point, Road


class AchievementAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class PointAdmin(admin.ModelAdmin):
    list_display = ("quantity", "character", "road")
    autocomplete_fields = ("character", "road")


class RoadAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Road, RoadAdmin)
