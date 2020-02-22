# Local imports
from django.db import models
from django.utils.text import slugify

# Third party
from ckeditor.fields import RichTextField

class Business(models.Model):
    RUBROS = (
        ('1', 'ALOJAMIENTO Y TURISMO'),
        ('2', 'ANIMALES Y PLANTAS DE JARDÍN'),
        ('3', 'CUIDADO PERSONAL, MODA Y COMPLEMENTOS'),
        ('4', 'CULTURA, DECORACIÓN, EXPOSICIÓN Y VENTA DE OBRAS ARTÍSTICAS'),
        ('5', 'DEPORTES'),
        ('6', 'DIVERSIÓN Y ENTRETENIMIENTO'),
        ('7', 'HOSTELERÍA'),
        ('8', 'ORGANIZACIÓN DE FIESTAS Y EVENTOS'),
        ('9', 'MISCELÁNEOS'),
    )
    header = models.ImageField(
        blank=True,
        upload_to='header/',
        default='header/default.jpg'
    )
    name = models.CharField(max_length=128)
    description = RichTextField()
    category = models.CharField(choices=RUBROS, max_length=1, default='1')
    register = models.URLField()
    topic = models.URLField()
    vault = models.URLField()
    slug = models.SlugField(max_length=140)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
