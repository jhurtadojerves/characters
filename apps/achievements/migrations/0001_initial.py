# Generated by Django 3.0.3 on 2020-03-10 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Achievement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                ("icon", models.ImageField(upload_to="achievements")),
                ("slug", models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Road",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, unique=True)),
                ("slug", models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="AchievementRequirements",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order", models.PositiveIntegerField()),
                (
                    "achievement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="mtm_achievements",
                        to="achievements.Achievement",
                    ),
                ),
                (
                    "requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="mtm_requirements",
                        to="achievements.Achievement",
                    ),
                ),
            ],
            options={
                "unique_together": {
                    ("achievement", "order"),
                    ("achievement", "requirement"),
                },
            },
        ),
        migrations.AddField(
            model_name="achievement",
            name="requirements",
            field=models.ManyToManyField(
                blank=True,
                through="achievements.AchievementRequirements",
                to="achievements.Achievement",
            ),
        ),
        migrations.AddField(
            model_name="achievement",
            name="roads",
            field=models.ManyToManyField(
                related_name="achievements", to="achievements.Road"
            ),
        ),
    ]