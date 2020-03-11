"""Register all models in admin"""

# Django
from django.contrib import admin

# Local
from .models import Achievement, AchievementRequirements, Road

admin.site.register(Achievement)
admin.site.register(AchievementRequirements)
admin.site.register(Road)
