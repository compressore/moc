# Generated by Django 3.0.3 on 2020-04-29 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stafdb', '0019_auto_20200429_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='license',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='space',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uploaded_by',
        ),
        migrations.DeleteModel(
            name='License',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
