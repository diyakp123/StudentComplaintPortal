# Generated by Django 5.0.6 on 2024-06-23 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.ForeignKey(default='unsolved', on_delete=django.db.models.deletion.CASCADE, to='complaint.complaintstatus'),
        ),
    ]
