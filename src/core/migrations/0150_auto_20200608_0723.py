# Generated by Django 3.0.3 on 2020-06-08 07:23

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0149_auto_20200608_0722'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='geocode',
            options={'ordering': ['depth', 'pk']},
        ),
        migrations.AlterModelManagers(
            name='geocode',
            managers=[
                ('objects_unfiltered', django.db.models.manager.Manager()),
            ],
        ),
    ]