# Generated by Django 3.1.3 on 2021-02-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210223_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termek',
            name='sorrend',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
