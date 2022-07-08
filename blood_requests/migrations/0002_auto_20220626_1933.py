# Generated by Django 3.2.13 on 2022-06-26 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_userprofile_blood_type"),
        ("requests", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="request",
            name="donors",
        ),
        migrations.AlterField(
            model_name="request",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blood_requests",
                to="users.userprofile",
            ),
        ),
    ]