# Generated by Django 3.1.3 on 2021-02-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210223_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategoria',
            name='borito',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images'),
        ),
    ]