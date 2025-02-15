# Generated by Django 4.2.11 on 2025-02-07 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vroom", "0002_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="category",
            field=models.CharField(
                choices=[
                    ("EDU", "Education"),
                    ("ENT", "Entertainment"),
                    ("SCI", "Science fition"),
                    ("SPT", "Sport"),
                ],
                default="EDU",
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.CharField(max_length=13, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="author",
            name="phone",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="video",
            name="published_date",
            field=models.DateField(null=True),
        ),
    ]
