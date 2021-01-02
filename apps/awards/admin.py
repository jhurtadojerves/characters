"""Register all models in admin"""

from django.contrib import admin, messages
from django.db import transaction
from django.utils.html import format_html

# Local
from .models import Award, Category, AccessToken, Voting, Winner

# Third party integration
from import_export.admin import ImportExportModelAdmin


class AwardAdmin(admin.ModelAdmin):
    """Config Admin from Award Model"""

    list_display = ("id", "name", "description", "opened")
    list_editable = ("name", "opened")
    actions = ("duplicate_categories",)

    def duplicate_categories(self, request, queryset):
        """"""
        with transaction.atomic():
            try:
                if len(queryset) > 1:
                    messages.error(
                        request, "No puedes realizar esta acción sobre varios objetos",
                    )
                    return False
                for instance in queryset:
                    if not instance.duplicate_to:
                        messages.error(
                            request,
                            "No configuraste el premio en el que vas a duplicar las categorías",
                        )
                        return False

                    if instance.opened:
                        messages.error(
                            request, "Antes de duplicar un premio tienes que cerrarlo",
                        )
                        return False
                    categories = instance.categories.all()
                    for category in categories:
                        new_category = Category.objects.create(
                            name=category.name,
                            description=category.description,
                            award=instance.duplicate_to,
                            self_voting=category.self_voting,
                            order=category.order,
                        )
                        if category.calculate_winners():
                            for winner in category.calculate_winners():
                                new_category.participants.add(winner["character"])
                        else:
                            for winner in category.participants.all():
                                new_category.participants.add(winner)
                    categories.update(status=False)
                    messages.success(
                        request,
                        "Las cetegorías se duplicaron correctamente y se asignaron los participantes",
                    )
                    return True
            except Exception as e:
                messages.error(
                    request, e.__str__(),
                )
                transaction.set_rollback(True)
                return False


class CategoryAdmin(ImportExportModelAdmin):
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
        "number_of_winners",
    )
    list_editable = (
        "name",
        "status",
        "max_options",
        "self_voting",
        "order",
        "number_of_winners",
    )
    filter_horizontal = ("participants", "winners")
    list_filter = ("award",)
    actions = ("define_winners", "show_winners")

    def show_winners(self, request, queryset):
        with transaction.atomic():
            try:
                for instance in queryset:
                    instance.show_winners = True
                    instance.save()
            except Exception as e:
                messages.error(
                    request, e.__str__(),
                )
                transaction.set_rollback(True)

    def define_winners(self, request, queryset):
        """"""
        with transaction.atomic():
            try:
                for instance in queryset:
                    instance.set_winners()
            except Exception as e:
                messages.error(
                    request, e.__str__(),
                )
                transaction.set_rollback(True)


class AccessTokenAdmin(admin.ModelAdmin):
    """Config access token model"""

    list_display = ["token", "user", "character", "get_url"]


class VotingAdmin(admin.ModelAdmin):
    """"""

    list_display = ("user", "award", "category", "show_selected_options")
    list_filter = ("user", "category")

    @staticmethod
    def show_selected_options(obj):
        return format_html(obj.admin_selected_options())


class WinnerAdmin(admin.ModelAdmin):
    """"""

    list_display = ("category", "character", "number_of_votes")
    list_filter = (
        "category__award",
        "category",
        "character",
    )


admin.site.register(Award, AwardAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(AccessToken, AccessTokenAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(Winner, WinnerAdmin)
