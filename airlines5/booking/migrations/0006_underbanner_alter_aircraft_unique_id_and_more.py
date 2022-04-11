# Generated by Django 4.0.3 on 2022-04-11 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_aircraft_unique_id_alter_airport_unique_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Underbanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(default='undefined', max_length=30)),
                ('description', models.TextField(default='description undefined', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='unique_id',
            field=models.CharField(default='1bcaa468-c8a4-4f22-9a18-edc9a2d9098a', max_length=36),
        ),
        migrations.AlterField(
            model_name='airport',
            name='unique_id',
            field=models.CharField(default='0b66483d-058e-440f-b515-7c36564e01ed', max_length=36),
        ),
        migrations.AlterField(
            model_name='fly',
            name='unique_id',
            field=models.CharField(default='caf97044-6b8c-45e7-9ade-6aafcbdd5868', max_length=36),
        ),
    ]
