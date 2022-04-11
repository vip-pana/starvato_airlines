# Generated by Django 4.0.3 on 2022-04-11 08:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_aircraft_alter_airport_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='unique_id',
            field=models.CharField(default='4e7dbf77-c8d5-4b01-8dd3-a18ca484babb', max_length=36),
        ),
        migrations.AlterField(
            model_name='airport',
            name='unique_id',
            field=models.CharField(default='d4cf97e4-7887-4f7f-b2d2-4f369565986a', max_length=36),
        ),
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default='d08233ae-de49-4ed3-8bc0-07eddf04e9b9', max_length=36)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('hour', models.TimeField(default=datetime.datetime.now)),
                ('aircraft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aircraft', to='booking.aircraft')),
                ('arrive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrive', to='booking.airport')),
                ('start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start', to='booking.airport')),
            ],
        ),
    ]
