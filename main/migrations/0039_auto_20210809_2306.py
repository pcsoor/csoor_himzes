# Generated by Django 3.1.3 on 2021-08-09 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_auto_20210805_2303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='color',
            options={'ordering': ['nev']},
        ),
        migrations.AddField(
            model_name='color',
            name='small_image',
            field=models.ImageField(blank=True, default='images/small_color.jpg', null=True, upload_to='images/'),
        ),
    ]
