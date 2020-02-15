from django.contrib import admin


from .models import Character


class CharacterAdmin(admin.ModelAdmin):
    list_display = "name", "nick", "range", "user"
    list_editable = ("user",)


admin.site.register(Character, CharacterAdmin)
