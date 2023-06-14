# Generated by Django 4.2.1 on 2023-06-13 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0004_alter_member_like_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="like_category",
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="member",
            name="profile",
            field=models.ImageField(
                blank=True, default=None, null=True, upload_to="member/images/%Y/%m/%d/"
            ),
        ),
    ]