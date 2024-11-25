# Generated by Django 5.0.6 on 2024-11-25 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_problemstatement_level_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MasterData",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("data", models.JSONField()),
            ],
        ),
        migrations.RenameField(
            model_name="problemstatement",
            old_name="query",
            new_name="sql_query",
        ),
        migrations.RenameField(
            model_name="problemstatement",
            old_name="tag",
            new_name="tags",
        ),
        migrations.AddField(
            model_name="problemstatement",
            name="output",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problemstatement",
            name="pandas_query",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problemstatement",
            name="pyspark_query",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="problemstatement",
            name="master_data",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.masterdata",
            ),
        ),
    ]