from django.db import models

# Create your models here.


class Business(models.model):
    name = models.CharField(max_length=128)
    register = models.URLField()
    topic = models.URLField()
    vault = models.URLField()
