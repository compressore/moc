# Generated by Django 3.0.6 on 2020-09-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0263_auto_20200908_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='zoteroitem',
            name='key',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]