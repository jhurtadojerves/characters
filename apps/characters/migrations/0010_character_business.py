# Generated by Django 2.2.5 on 2019-09-10 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0002_auto_20190909_2348"),
        ("characters", "0009_auto_20190908_2040"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="business",
            field=models.ManyToManyField(
                related_name="characters", to="business.Business"
            ),
        ),
    ]
