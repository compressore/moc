# Generated by Django 3.0.3 on 2020-03-13 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200313_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='articledesign',
            name='custom_css',
            field=models.TextField(blank=True, null=True),
        ),
    ]