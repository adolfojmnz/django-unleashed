# Generated by Django 4.0 on 2021-12-23 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0007_newslink_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together={('slug', 'startup')},
        ),
    ]
