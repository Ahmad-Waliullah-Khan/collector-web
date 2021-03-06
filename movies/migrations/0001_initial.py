# Generated by Django 3.0.3 on 2020-02-27 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('review', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('WATCHING', 'Watching'), ('COMPLETED', 'Completed'), ('TO-WATCH', 'To-Watch')], default='WATCHING', max_length=50)),
                ('collected_on', models.CharField(choices=[('PHYSICAL', 'Own Physically'), ('DIGITAL', 'Own Digitally')], default='PHYSICAL', max_length=50)),
                ('watched', models.BooleanField(default=False)),
                ('started_watching_on', models.DateTimeField(blank=True, null=True)),
                ('completed_watching_on', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
                'db_table': 'movies',
                'ordering': ['-updated_at'],
            },
        ),
    ]
