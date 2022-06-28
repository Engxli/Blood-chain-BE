# Generated by Django 3.2.13 on 2022-06-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donations", "0002_donation_request"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donation",
            name="status",
            field=models.IntegerField(
                choices=[(1, "Pending"), (2, "Complete"), (3, "Canceled")]
            ),
        ),
    ]
