# Generated by Django 4.1.7 on 2023-03-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0008_alter_category_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessageuser",
            name="friend_type",
            field=models.CharField(
                choices=[
                    ("buddies", "Buddies"),
                    ("family", "Family"),
                    ("co-workers", "Co-Workers"),
                ],
                default="buddies",
                max_length=50,
            ),
        ),
    ]
