# Generated by Django 3.0.3 on 2020-05-13 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0098_auto_20200513_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='priority',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], db_index=True, default=2),
        ),
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.IntegerField(choices=[(1, 'Open'), (2, 'Completed'), (3, 'Discarded'), (4, 'On Hold'), (5, 'In Progress')], db_index=True, default=1),
        ),
    ]
