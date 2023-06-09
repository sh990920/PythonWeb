# Generated by Django 4.2.1 on 2023-06-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Show",
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
                ("showTitle", models.CharField(max_length=200)),
                ("showCategory", models.CharField(max_length=200)),
                ("showPeriod", models.CharField(max_length=200)),
                ("showTime", models.CharField(max_length=200)),
                ("showPlace", models.CharField(max_length=200)),
                ("showAgeGroup", models.CharField(max_length=200, null=True)),
                ("ticketPrice", models.IntegerField()),
                ("showCast", models.CharField(max_length=200)),
            ],
        ),
    ]
