# Generated by Django 3.0.7 on 2020-10-17 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20201013_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='service_category',
            new_name='serviceCategory',
        ),
    ]
