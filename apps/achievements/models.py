"""Models for the Achievements app"""

# Django
from django.db import models
from django.db.models.signals import post_save

# Local
from utils.create_unique_slug import create_unique_slug


class Road(models.Model):
    """Model to create custom roads for users"""

    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, editable=False)


class Achievement(models.Model):
    """Model to create custom achievements"""

    name = models.CharField(max_length=128, unique=True)
    roads = models.ManyToManyField(Road, related_name="achievements")
    requirements = models.ManyToManyField(
        "self", blank=True, through="AchievementRequirements", symmetrical=False
    )
    icon = models.ImageField(upload_to="achievements")
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.name


class AchievementRequirements(models.Model):
    """Intermediate table many to many relationship"""

    achievement = models.ForeignKey(
        Achievement, related_name="mtm_achievements", on_delete=models.PROTECT
    )
    requirement = models.ForeignKey(
        Achievement, related_name="mtm_requirements", on_delete=models.PROTECT
    )
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = [["achievement", "requirement"], ["achievement", "order"]]


post_save.connect(create_unique_slug, Road)
post_save.connect(create_unique_slug, Achievement)
