# Generated by Django 4.1.4 on 2023-01-27 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name="category",
            unique_together={("country", "name")},
        ),
    ]
