# Generated by Django 3.1.7 on 2021-04-12 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_food_food_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="food_price",
            field=models.FloatField(default=0),
        ),
    ]
