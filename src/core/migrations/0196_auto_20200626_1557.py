# Generated by Django 3.0.6 on 2020-06-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0195_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='core.Document'),
        ),
    ]