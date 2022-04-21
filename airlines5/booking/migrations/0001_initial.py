# Generated by Django 4.0.3 on 2022-04-21 10:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=36)),
                ('model', models.CharField(max_length=100)),
                ('seats', models.IntegerField(default=60)),
                ('km_tot', models.IntegerField(default=0)),
                ('pilots_num', models.IntegerField(default=4)),
                ('team_num', models.IntegerField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=36)),
                ('name', models.CharField(max_length=250)),
                ('localcode', models.IntegerField()),
                ('country', models.CharField(max_length=250)),
                ('region', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_id', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('person', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=1, max_length=2)),
                ('arrive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='S_arrive', to='booking.airport')),
                ('start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='S_start', to='booking.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Fly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, default='0', max_length=36)),
                ('free_seats', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('hour', models.TimeField(default=datetime.datetime.now)),
                ('price', models.FloatField(default=5.0)),
                ('aircraft', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aircraft', to='booking.aircraft')),
                ('arrive', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrive', to='booking.airport')),
                ('start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='start', to='booking.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, default='0', max_length=36)),
                ('status', models.CharField(blank=True, max_length=15)),
                ('airC_seat', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('fly', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fly_booking', to='booking.fly')),
            ],
        ),
    ]
