# Generated by Django 3.0.3 on 2020-02-27 12:59

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
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_title', models.CharField(max_length=50)),
                ('review', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('WATCHING', 'Watching'), ('COMPLETED', 'Completed'), ('TO-WATCH', 'To-Watch')], default='WATCHING', max_length=50)),
                ('collected_on', models.CharField(choices=[('PHYSICAL', 'Own Physically'), ('DIGITAL', 'Own Digitally')], default='PHYSICAL', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('watching', models.BooleanField(default=True)),
                ('started_wathcing_on', models.DateTimeField()),
                ('completed_wathcing_on', models.DateTimeField()),
                ('seasons_watched', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Show',
                'verbose_name_plural': 'Shows',
                'db_table': 'shows',
                'ordering': ['-updated_at'],
            },
        ),
    ]
