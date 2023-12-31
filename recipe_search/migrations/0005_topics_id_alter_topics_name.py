# Generated by Django 4.2.5 on 2023-10-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipe_search", "0004_remove_recipes_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="topics",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="topics",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]
