# Generated by Django 4.2.1 on 2023-06-13 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0002_alter_member_like_category_alter_member_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="password",
            field=models.CharField(max_length=200),
        ),
    ]
