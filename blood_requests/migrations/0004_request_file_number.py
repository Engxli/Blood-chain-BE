# Generated by Django 3.2.13 on 2022-07-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requests", "0003_auto_20220629_0901"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="file_number",
            field=models.IntegerField(null=True),
        ),
    ]
