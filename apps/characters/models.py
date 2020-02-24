# Core imports
from django.db import models
from django.utils.text import slugify

# Local
from apps.business.models import Business


class Character(models.Model):
    range_choices = (
        ("1", "Initie"),
        ("2", "Legionario"),
        ("3", "Templario"),
        ("4", "Knight"),
        ("5", "Demon Hunter"),
        ("6", "Líder"),
    )

    name = models.CharField(max_length=128, verbose_name="Nombre del Personaje")
    avatar = models.ImageField(
        blank=True, upload_to="avatar/", default="avatar/default.jpg"
    )
    nick = models.CharField(max_length=128, unique=True, verbose_name="Nick de Usuario")
    range = models.CharField(
        choices=range_choices,
        max_length=1,
        default="1",
        verbose_name="Rango en el Bando",
    )
    is_lieutenant = models.BooleanField(
        default=False, verbose_name="¿Es Lugar Teniente?"
    )
    user = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Nombre Real"
    )
    characteristics = models.TextField(
        verbose_name="Características Principales del Personaje"
    )
    job = models.CharField(
        max_length=256, blank=True, null=True, verbose_name="Trabajo en el CMI"
    )
    job_description = models.TextField(
        blank=True, null=True, verbose_name="Información adicional sobre el trabajo"
    )
    patronus = models.TextField(verbose_name="Descripción del Patronus")
    wand = models.TextField(verbose_name="Descripción de la Varita Mágica")
    secondary_characters = models.URLField(
        blank=True,
        null=True,
        verbose_name="Link a las Fichas de los Personajes Secundario",
    )
    character_card = models.URLField(verbose_name="Link a la Ficha de Personaje")
    vault = models.URLField("Link a la Bóveda")
    storage_vault = models.URLField("Link a la Bóveda Trastero")
    business = models.ManyToManyField(Business, related_name="characters", blank=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=140)

    def __str__(self):
        return f"{self.nick}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nick)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ("nick",)
