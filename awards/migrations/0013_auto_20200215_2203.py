# Generated by Django 3.0.3 on 2020-02-15 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0015_auto_20200215_2155"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("awards", "0012_accesstoken_character"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accesstoken",
            name="character",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="token",
                to="characters.Character",
            ),
        ),
        migrations.AlterField(
            model_name="accesstoken",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="token",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
