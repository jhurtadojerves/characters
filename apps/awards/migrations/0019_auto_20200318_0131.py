# Generated by Django 3.0.3 on 2020-03-18 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0018_auto_20200301_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='winner',
            options={'ordering': ('-number_of_votes',)},
        ),
    ]
