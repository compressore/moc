# Generated by Django 3.0.6 on 2020-06-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0189_auto_20200626_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='subscribers',
            field=models.ManyToManyField(blank=True, to='core.People'),
        ),
    ]
