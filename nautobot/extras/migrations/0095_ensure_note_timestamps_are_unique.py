# Generated by Django 3.2.20 on 2023-07-18 14:50

import secrets

from datetime import timedelta
from django.db import migrations
from django.db import models


def ensure_note_created_timestamps_are_unique(apps, schema_editor):
    Note = apps.get_model("extras", "Note")
    natural_key_fields = ["assigned_object_type", "assigned_object_id", "user_name", "created"]

    # We append some random milliseconds of time to avoid duplicate timestamps for Note objects' created field.

    duplicate_records = (
        Note.objects.values(*natural_key_fields).order_by().annotate(count=models.Count("pk")).filter(count__gt=1)
    )
    for duplicate_record in duplicate_records:
        duplicate_record.pop("count")
        duplicate_notes = Note.objects.filter(**duplicate_record)
        for note in duplicate_notes:
            random_milliseconds = secrets.randbelow(1000)
            note.created += timedelta(milliseconds=random_milliseconds)
            note.save()


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0094_alter_objectchange_unique_together"),
    ]

    operations = [
        migrations.RunPython(ensure_note_created_timestamps_are_unique, migrations.RunPython.noop),
    ]
