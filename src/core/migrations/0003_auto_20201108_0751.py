# Generated by Django 3.1.2 on 2020-11-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201105_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geocodescheme',
            name='type',
            field=models.IntegerField(choices=[(1, 'National subdivisions'), (2, 'Infrastructure'), (3, 'Administrative areas')], db_index=True, default=3),
        ),
    ]
