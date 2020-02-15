"""Models to awards app"""

# python
from uuid import uuid4
from django.shortcuts import reverse

# Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
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
    max_options = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name


class AccessToken(models.Model):
    """Create a random token to voting"""

    token = models.UUIDField(unique=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_url(self):
        return (
            f"https://manifiesto.ordendelfenix.xyz{reverse('login', args=[self.token])}"
        )


class Voting(models.Model):
    """User voting to all of award categories"""

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="votes")
    category = models.ForeignKey(
        Category, related_name="votes", on_delete=models.PROTECT
    )
    selected_options = models.ManyToManyField(
        Character, verbose_name="Seleccionar las opciones"
    )

    class Meta:
        unique_together = ("user", "category")


def create_unique_slug(sender, instance, created, **kwargs):
    """Create and update slug"""
    if created:
        instance.slug = slugify(f"{instance.pk} {instance.name}")
        instance.save()
    else:
        slug = instance.slug
        instance.slug = slugify(f"{instance.pk} {instance.name}")
        if not slug == instance.slug:
            instance.save()


post_save.connect(create_unique_slug, Award)
post_save.connect(create_unique_slug, Category)
