# Generated by Django 3.2.5 on 2021-07-29 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_liked_songs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='liked_songs',
            old_name='liked_songs_json',
            new_name='liked',
        ),
    ]
