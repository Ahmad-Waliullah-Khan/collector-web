# Generated by Django 3.0.3 on 2020-02-28 21:07

import comics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comicbooks',
            name='cover_image',
            field=models.FileField(blank=True, null=True, upload_to=comics.models.get_file_path),
        ),
    ]
