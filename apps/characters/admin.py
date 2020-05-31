"""Admin Characters models"""
from django.contrib import admin

# Third Party Integration
from import_export.admin import ImportExportModelAdmin

# Local imports
from .models import Character


class CharacterAdmin(ImportExportModelAdmin):
    list_display = "name", "nick", "range", "user"
    list_editable = ("user",)
    filter_horizontal = ("achievements", "business")
    search_fields = ("name", "nick", "user")


admin.site.register(Character, CharacterAdmin)
