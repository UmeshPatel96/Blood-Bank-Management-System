# Generated by Django 5.0.3 on 2024-04-02 08:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raktkosh', '0003_bloodrequest_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(default='Nothing', max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raktkosh.userprofile')),
            ],
        ),
    ]
