# Generated by Django 4.2.1 on 2023-06-14 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("member", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chat",
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
                ("mettingIdx", models.IntegerField()),
                ("content", models.CharField(max_length=200)),
                ("write_time", models.DateTimeField(auto_now_add=True)),
                (
                    "memberIdx",
                    models.ForeignKey(
                        db_column="memberIdx",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="member.member",
                    ),
                ),
            ],
        ),
    ]
