# Generated by Django 5.0.6 on 2024-06-26 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_contactus'),
        ('complaint', '0003_alter_complaint_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('opinion', models.TextField()),
                ('complaintid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.complaint')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
    ]
