# Generated by Django 4.1.9 on 2023-05-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='isdone',
            field=models.BooleanField(default=False),
        ),
    ]
