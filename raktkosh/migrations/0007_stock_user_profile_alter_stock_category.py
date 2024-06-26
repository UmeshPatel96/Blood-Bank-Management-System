# Generated by Django 5.0.3 on 2024-04-07 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raktkosh', '0006_stock_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='user_profile',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='raktkosh.userprofile'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raktkosh.category'),
        ),
    ]
