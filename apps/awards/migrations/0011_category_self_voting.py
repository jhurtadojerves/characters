# Generated by Django 3.0.3 on 2020-02-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("awards", "0010_auto_20200213_0355"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="self_voting",
            field=models.BooleanField(default=True),
        ),
    ]