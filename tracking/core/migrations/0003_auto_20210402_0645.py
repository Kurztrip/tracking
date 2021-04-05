# Generated by Django 3.1.7 on 2021-04-02 06:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210402_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='p_latitudes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='route',
            name='p_longitudes',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, null=True, size=None),
        ),
    ]
