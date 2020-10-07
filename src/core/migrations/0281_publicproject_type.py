# Generated by Django 3.1.2 on 2020-10-07 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0280_auto_20201005_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicproject',
            name='type',
            field=models.CharField(choices=[('thesis', 'Thesis project'), ('research', 'Research project')], default='research', max_length=20),
        ),
    ]
