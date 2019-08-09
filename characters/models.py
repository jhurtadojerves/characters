from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=128)
    nick = models.CharField(max_length=128, unique=True)
    user = models.CharField(max_length=128, blank=True, null=True)
    characteristics = models.TextField()
    job = models.CharField(max_length=256, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    patronus = models.TextField()
    wand = models.TextField()
    secondary_characters = models.URLField()
