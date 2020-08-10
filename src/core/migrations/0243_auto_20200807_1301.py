# Generated by Django 3.0.6 on 2020-08-07 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0242_auto_20200806_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryitem',
            name='is_part_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='core.LibraryItem'),
        ),
    ]