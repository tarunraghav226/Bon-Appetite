# Generated by Django 3.1.7 on 2021-04-12 05:44

from django.db import migrations, models

import app.models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_auto_20210412_0534"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="food_image",
            field=models.ImageField(
                default=None, upload_to=app.models.get_image_address
            ),
        ),
    ]
