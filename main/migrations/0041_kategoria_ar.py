# Generated by Django 3.2.6 on 2021-08-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_auto_20210809_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategoria',
            name='ar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]