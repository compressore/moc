# Generated by Django 3.0.6 on 2020-06-20 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0172_work_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='url',
        ),
    ]