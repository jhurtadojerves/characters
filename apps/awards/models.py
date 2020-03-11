"""Models to awards app"""

# python
from uuid import uuid4
from django.shortcuts import reverse

# Django
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

# Local
from apps.characters.models import Character
from utils.create_unique_slug import create_unique_slug


class Award(models.Model):
    """Model to create award"""

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    opened = models.BooleanField(default=False)
    duplicate_to = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )
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
    self_voting = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=1)
    winners = models.ManyToManyField(
        Character, related_name="winners", through="Winner"
    )
    number_of_winners = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    def calculate_winners(self):
        voting = None
        if self.votes.all():
            voting = (
                self.votes.all()
                .values("selected_options")
                .annotate(number_of_votes=models.Count("selected_options"))
                .filter(number_of_votes__gt=0)
                .order_by("-number_of_votes")
            )
            if len(voting) >= self.number_of_winners:
                max_indice = self.number_of_winners - 1
                for i in range(max_indice, len(voting) - 1):
                    if (
                        voting[max_indice]["number_of_votes"]
                        == voting[max_indice + 1]["number_of_votes"]
                    ):
                        max_indice = max_indice + 1
                max_indice = max_indice + 1
                voting = voting[:max_indice]
            for character in voting:
                character.update(
                    {
                        "character": Character.objects.get(
                            pk=character["selected_options"]
                        )
                    }
                )
                del character["selected_options"]
        return voting

    class Meta:
        ordering = ("order", "id")


class AccessToken(models.Model):
    """Create a random token to voting"""

    token = models.UUIDField(unique=True, default=uuid4, editable=False,)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="token")
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, null=True, related_name="token"
    )

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

    def award(self):
        return self.category.award

    def admin_selected_options(self):
        selected_options = ""
        for selected in self.selected_options.all():
            selected_options += f"<li>{selected}</li>"
        return f"<ul>{selected_options}</ul>"

    class Meta:
        unique_together = ("user", "category")


class Winner(models.Model):
    """Select winners"""

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    character = models.ForeignKey(Character, on_delete=models.PROTECT)
    number_of_votes = models.PositiveIntegerField()


post_save.connect(create_unique_slug, Award)
post_save.connect(create_unique_slug, Category)
