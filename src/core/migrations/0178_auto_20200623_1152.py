# Generated by Django 3.0.6 on 2020-06-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0177_eurostatdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eurostatdb',
            name='values',
        ),
        migrations.AddField(
            model_name='eurostatdb',
            name='title',
            field=models.CharField(default='hi', max_length=255),
            preserve_default=False,
        ),
    ]
