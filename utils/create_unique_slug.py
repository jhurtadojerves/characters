"""Create a unique slug from objects"""

from django.utils.text import slugify


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
