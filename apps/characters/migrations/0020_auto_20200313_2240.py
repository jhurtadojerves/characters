# Generated by Django 3.0.3 on 2020-03-13 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0019_auto_20200311_0210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="avatar",
            field=models.ImageField(
                blank=True, default="avatar/fenix.png", upload_to="avatar/"
            ),
        ),
    ]
