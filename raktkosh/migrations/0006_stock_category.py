# Generated by Django 5.0.3 on 2024-04-04 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raktkosh', '0005_rename_donor_blooddonate_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='raktkosh.category'),
        ),
    ]