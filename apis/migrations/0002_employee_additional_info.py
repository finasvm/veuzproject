# Generated by Django 5.1.2 on 2024-11-05 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='additional_info',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
