# Generated by Django 2.2.4 on 2019-09-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_character_is_lieutenant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='is_lieutenant',
            field=models.BooleanField(default=False, verbose_name='¿Es Lugar Teniente?'),
        ),
    ]
