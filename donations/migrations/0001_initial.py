# Generated by Django 3.2.13 on 2022-06-29 21:30

from typing import Any

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list[Any] = []

    operations = [
        migrations.CreateModel(
            name="Donation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[
                            (1, "Pending"),
                            (2, "Complete"),
                            (3, "Canceled"),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
