# Generated by Django 3.0.3 on 2020-02-27 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv', '0002_auto_20200227_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shows',
            old_name='completed_wathcing_on',
            new_name='completed_watching_on',
        ),
        migrations.RenameField(
            model_name='shows',
            old_name='started_wathcing_on',
            new_name='started_watching_on',
        ),
    ]