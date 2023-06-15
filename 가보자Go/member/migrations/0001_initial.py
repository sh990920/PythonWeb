# Generated by Django 4.2.1 on 2023-06-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("memberId", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=200)),
                ("nickname", models.CharField(max_length=20, unique=True)),
                (
                    "like_category",
                    models.CharField(
                        blank=True, default=None, max_length=20, null=True
                    ),
                ),
                (
                    "profile",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="member/images/%Y/%m/%d/",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
