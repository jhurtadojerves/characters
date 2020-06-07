"""Register Simple Template Tag"""

# Django
from django import template
from django.db.models import Sum

# Local
from apps.achievements.models import Point, Road

register = template.Library()


@register.simple_tag
def icon(character, achievement):

    filtered_achievement = character.achievements.filter(pk=achievement.pk)
    if filtered_achievement.exists():
        return {"css": "", "legend": "Obtenido"}
    return {"css": "opacity:25%;", "legend": "No obtenido"}


@register.simple_tag
def icon_bbcode(character, achievement):

    filtered_achievement = character.achievements.filter(pk=achievement.pk)
    if filtered_achievement.exists():
        return {"url": achievement.icon_principal.url, "legend": "Obtenido"}
    return {"url": achievement.icon_secondary.url, "legend": "No obtenido"}


@register.simple_tag
def road_point(character, road):
    get_road = Road.objects.get(name=road)
    points = Point.objects.filter(character=character, road=get_road).aggregate(
        Sum("quantity")
    )["quantity__sum"]
    if not points:
        return "0"
    return points
