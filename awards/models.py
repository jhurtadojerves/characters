"""Models to awards app"""

# python
from uuid import uuid4

# Django
from django.db import models
from django.utils.text import slugify

# Local
from characters.models import Character


class Award(models.Model):
    """Model to create award"""

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    slug = models.SlugField(max_length=512, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Category(models.Model):
    """Define all categories of award"""

    name = models.CharField(max_length=64)
    description = models.TextField()
    award = models.ForeignKey(
        Award, related_name="categories", on_delete=models.PROTECT
    )
    participants = models.ManyToManyField(
        Character, related_name="categories", blank=True
    )
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=512, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class AccessToken(models.Model):
    """Create a random token to voting"""

    token = models.UUIDField(unique=True, default=uuid4, editable=False)


class Voting(models.Model):
    """User voting to all of award categories"""

    user = models.ForeignKey(AccessToken, on_delete=models.PROTECT)
    category = models.ForeignKey(
        Category, related_name="votes", on_delete=models.PROTECT
    )
    selected_option = models.ForeignKey(Character, on_delete=models.PROTECT)
