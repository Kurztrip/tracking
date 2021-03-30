# Generated by Django 3.1.7 on 2021-03-29 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('location', models.IntegerField()),
                ('state', models.CharField(max_length=10)),
                ('estimated_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]