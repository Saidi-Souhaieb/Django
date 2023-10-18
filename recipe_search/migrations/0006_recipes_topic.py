# Generated by Django 4.2.5 on 2023-10-16 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("recipe_search", "0005_topics_id_alter_topics_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipes",
            name="topic",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="recipe_search.topics",
            ),
            preserve_default=False,
        ),
    ]
