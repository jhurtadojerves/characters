"""Models for the Achievements app"""

# Django
from django.db import models
from django.db.models.signals import post_save
from django.db.models import Sum
from django.utils.html import mark_safe

# Local
from utils.create_unique_slug import create_unique_slug

LIST_MONTHS = {
    0: "enero",
    1: "febrero",
    2: "marzo",
    3: "abril",
    4: "mayo",
    5: "junio",
    6: "julio",
    7: "agosto",
    8: "septiembre",
    9: "octubre",
    10: "noviembre",
    11: "diciembre",
}


class Road(models.Model):
    """Model to create custom roads for users"""

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name


class Achievement(models.Model):
    """Model to create custom achievements"""

    name = models.CharField(max_length=128, unique=True)
    road = models.ForeignKey(
        Road, related_name="achievements", on_delete=models.CASCADE
    )
    points = models.PositiveIntegerField(default=1)
    icon_principal = models.ImageField(upload_to="achievements")
    icon_secondary = models.ImageField(upload_to="achievements")
    slug = models.SlugField(unique=True, editable=False)

    def get_icon_principal(self):
        return mark_safe(f"<img src='{self.icon_principal.url}' />")

    def get_icon_secondary(self):
        return mark_safe(f"<img src='{self.icon_secondary.url}' />")

    def __str__(self):
        return self.name


class Point(models.Model):
    """Model to assign points to character"""

    quantity = models.PositiveIntegerField()
    character = models.ForeignKey(
        "characters.Character", related_name="points", on_delete=models.CASCADE
    )
    reason = models.CharField(max_length=256)
    creation_date = models.DateField()
    road = models.ForeignKey(Road, related_name="points", on_delete=models.CASCADE)

    def get_month(self):
        return LIST_MONTHS[self.creation_date.month]

    def get_year(self):
        return self.creation_date.year


def calculate_achievements(sender, instance, created, **kwargs):
    """Assign achievements in create or save points"""
    user_points = Point.objects.filter(
        character=instance.character, road=instance.road
    ).aggregate(Sum("quantity"))
    user_achievements = []
    user_achievements_all = instance.character.achievements.all()
    if user_achievements_all.exists():
        user_achievements = list(user_achievements_all.values_list("pk", flat=True))
    achievements = Achievement.objects.filter(
        road=instance.road, points__lte=user_points["quantity__sum"],
    ).exclude(id__in=user_achievements,)

    for achievement in achievements:
        instance.character.achievements.add(achievement)


post_save.connect(create_unique_slug, Achievement)
post_save.connect(create_unique_slug, Road)

post_save.connect(calculate_achievements, Point)
