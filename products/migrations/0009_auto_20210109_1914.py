# Generated by Django 3.1.4 on 2021-01-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210109_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
