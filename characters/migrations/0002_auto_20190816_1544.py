# Generated by Django 2.2.4 on 2019-08-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='secondary_characters',
            field=models.URLField(blank=True, null=True),
        ),
    ]
