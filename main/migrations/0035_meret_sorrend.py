# Generated by Django 3.1.3 on 2021-08-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20210804_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='meret',
            name='sorrend',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]