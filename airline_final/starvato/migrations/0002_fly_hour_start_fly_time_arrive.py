# Generated by Django 4.0.4 on 2022-04-26 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('starvato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='hour_start',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='fly',
            name='time_arrive',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
