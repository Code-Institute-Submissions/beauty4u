# Generated by Django 3.0.7 on 2020-12-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20201221_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('position', models.CharField(blank=True, max_length=250, null=True)),
                ('available', models.BooleanField(blank=True, default=True, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Staff Members',
            },
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
