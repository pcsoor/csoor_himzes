# Generated by Django 3.1.3 on 2021-08-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20210805_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='azonosito_szin',
        ),
        migrations.AddField(
            model_name='color',
            name='sotet',
            field=models.BooleanField(default=False),
        ),
    ]
