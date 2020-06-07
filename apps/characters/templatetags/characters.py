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