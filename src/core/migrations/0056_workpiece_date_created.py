# Generated by Django 3.0.3 on 2020-05-03 09:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20200503_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpiece',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]