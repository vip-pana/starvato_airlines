# Generated by Django 4.0.3 on 2022-04-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_aircraft_unique_id_alter_airport_unique_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='unique_id',
            field=models.CharField(default='732df2b8-1a3a-4da5-92f4-123b47a78df1', max_length=36),
        ),
        migrations.AlterField(
            model_name='airport',
            name='unique_id',
            field=models.CharField(default='e5f07741-e812-43f5-8d40-bc8d4ea8ebf0', max_length=36),
        ),
        migrations.AlterField(
            model_name='fly',
            name='unique_id',
            field=models.CharField(default='fb66e20c-eaa8-408a-96df-803f3d937fed', max_length=36),
        ),
    ]
