# Generated by Django 3.0.3 on 2020-05-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_auto_20200503_1351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraryitem',
            name='authorlist',
        ),
        migrations.AddField(
            model_name='libraryitem',
            name='author_list',
            field=models.TextField(blank=True, null=True),
        ),
    ]