# Generated by Django 3.2.7 on 2021-09-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image_cover',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images/'),
        ),
    ]