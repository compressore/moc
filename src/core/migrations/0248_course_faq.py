# Generated by Django 3.0.6 on 2020-08-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0247_eurostatdb_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='faq',
            field=models.TextField(blank=True, null=True),
        ),
    ]
