# Generated by Django 3.1.3 on 2021-02-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210223_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termek',
            name='sorrend',
            field=models.IntegerField(default=0),
        ),
    ]
