# Generated by Django 3.0.3 on 2020-05-31 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0005_auto_20200531_0145"),
    ]

    operations = [
        migrations.AddField(
            model_name="point",
            name="reason",
            field=models.CharField(default="", max_length=256),
            preserve_default=False,
        ),
    ]
