# Generated by Django 4.0.3 on 2022-04-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_search_have_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='have_return',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
