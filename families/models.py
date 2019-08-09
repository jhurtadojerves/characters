from django.db import models

# Create your models here.


class Family(models.model):
    name = models.CharField(max_length=128)
    register = models.URLField()
    topic = models.URLField()
    vault = models.URLField()
