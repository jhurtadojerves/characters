# Generated by Django 3.0.3 on 2020-06-30 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0006_point_reason"),
    ]

    operations = [
        migrations.AddField(
            model_name="point",
            name="creation_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
