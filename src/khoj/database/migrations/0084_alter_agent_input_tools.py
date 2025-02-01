# Generated by Django 5.0.10 on 2025-01-28 23:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0083_alter_agent_output_modes_alter_agent_personality_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="input_tools",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("general", "General"),
                        ("online", "Online"),
                        ("notes", "Notes"),
                        ("webpage", "Webpage"),
                        ("code", "Code"),
                    ],
                    max_length=200,
                ),
                blank=True,
                default=list,
                null=True,
                size=None,
            ),
        ),
    ]
