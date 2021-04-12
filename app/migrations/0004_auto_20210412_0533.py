# Generated by Django 3.1.7 on 2021-04-12 05:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0003_auto_20210406_1456"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop",
            name="shop_name",
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name="shop",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
