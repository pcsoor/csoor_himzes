# Generated by Django 3.1.3 on 2021-08-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20210804_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategoria',
            name='borito',
            field=models.ImageField(blank=True, default='images/placeholder.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='kategoria',
            name='image',
            field=models.ImageField(blank=True, default='images/placeholder.jpg', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='szin',
            name='image',
            field=models.ImageField(blank=True, default='images/placeholder.jpg', null=True, upload_to='images/'),
        ),
    ]
