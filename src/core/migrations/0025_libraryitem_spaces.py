# Generated by Django 3.0.3 on 2020-04-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stafdb', '0016_referencespace_geocodes'),
        ('core', '0024_auto_20200427_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryitem',
            name='spaces',
            field=models.ManyToManyField(blank=True, to='stafdb.ReferenceSpace'),
        ),
    ]