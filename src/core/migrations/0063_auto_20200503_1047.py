# Generated by Django 3.0.3 on 2020-05-03 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_auto_20200503_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forummessage',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='webpage',
            name='parent',
        ),
        migrations.AddField(
            model_name='record',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Record'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('planned', 'Planned'), ('ongoing', 'Ongoing'), ('finished', 'Finished'), ('cancelled', 'Cancelled')], default='ongoing', max_length=20),
        ),
    ]
