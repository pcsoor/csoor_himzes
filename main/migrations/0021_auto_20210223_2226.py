# Generated by Django 3.1.3 on 2021-02-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_termek_sorrend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termek',
            name='sorrend',
            field=models.IntegerField(),
        ),
    ]
