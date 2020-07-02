# Generated by Django 3.0.6 on 2020-07-01 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0207_auto_20200630_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='workactivity',
            name='url',
            field=models.URLField(blank=True, help_text='Is there a specific link a user could go to in order to work on this task? If so, put it here', null=True),
        ),
    ]