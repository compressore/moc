# Generated by Django 3.0.6 on 2020-06-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0176_message_posted_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='EurostatDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('last_update', models.CharField(blank=True, max_length=255, null=True)),
                ('data_start', models.CharField(blank=True, max_length=255, null=True)),
                ('data_end', models.CharField(blank=True, max_length=255, null=True)),
                ('values', models.CharField(blank=True, max_length=255, null=True)),
                ('is_reviewed', models.BooleanField(db_index=True, default=False)),
                ('is_approved', models.BooleanField(blank=True, db_index=True, null=True)),
                ('is_denied', models.BooleanField(blank=True, db_index=True, null=True)),
            ],
        ),
    ]
