"""Register Simple Template Tag"""

# Django
from django import template


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
