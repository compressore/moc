# Generated by Django 3.0.3 on 2020-04-27 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_record_old_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryitem',
            name='published_in',
            field=models.ForeignKey(blank=True, help_text='If the journal does not appear in the list, please leave empty and add the name in the comments', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='core.Journal'),
        ),
    ]
