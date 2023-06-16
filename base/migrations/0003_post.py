# Generated by Django 4.2.2 on 2023-06-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_user_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("email", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
    ]
