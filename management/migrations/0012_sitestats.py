# Generated by Django 3.0.7 on 2020-12-30 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_coupons_minspend'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(blank=True, max_length=250, null=True)),
                ('value', models.IntegerField(blank=True, default='0', null=True)),
            ],
            options={
                'verbose_name_plural': 'Site Stats',
            },
        ),
    ]
