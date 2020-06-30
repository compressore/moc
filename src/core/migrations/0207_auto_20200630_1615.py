# Generated by Django 3.0.6 on 2020-06-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0206_activitycatalog_original_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='description_html',
            field=models.TextField(blank=True, help_text='Do not edit... auto-generated by the system', null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='url',
            field=models.URLField(blank=True, help_text='Is there a specific link a user could go to in order to work on this task? If so, put it here', null=True),
        ),
    ]