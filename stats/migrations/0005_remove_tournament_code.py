# Generated by Django 4.0.4 on 2022-06-06 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0004_tournament_slug_tournament_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='code',
        ),
    ]
