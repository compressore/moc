# Generated by Django 3.0.3 on 2020-05-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20200501_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='slug',
            field=models.SlugField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]