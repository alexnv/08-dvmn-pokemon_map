# Generated by Django 3.1.14 on 2023-02-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_pokemon_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.TextField(blank=True),
        ),
    ]
