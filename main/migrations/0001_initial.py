# Generated by Django 3.1.3 on 2021-02-19 14:06

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images')),
                ('status', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.kategoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Szin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='images')),
                ('hex', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Termek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=255)),
                ('anyag', models.CharField(blank=True, max_length=255, null=True)),
                ('osszetetel', models.CharField(blank=True, max_length=255, null=True)),
                ('tomeg', models.CharField(blank=True, max_length=255, null=True)),
                ('kulso', models.CharField(blank=True, max_length=255, null=True)),
                ('akcios_ar', models.IntegerField(blank=True, null=True)),
                ('ujdonsag', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termekimage', to='main.szin')),
                ('kategoria_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kategoria')),
                ('meret_id', models.ManyToManyField(blank=True, related_name='meret', to='main.Meret')),
                ('szin_id', models.ManyToManyField(blank=True, related_name='termekszin', to='main.Szin')),
            ],
        ),
    ]
