# Generated by Django 5.1.5 on 2025-01-17 18:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0004_rename_desccription_teacher_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
