# Generated by Django 5.1.5 on 2025-01-17 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="teacher",
            old_name="datre_joined",
            new_name="date_joined",
        ),
    ]
