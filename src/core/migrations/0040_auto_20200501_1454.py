# Generated by Django 3.0.3 on 2020-05-01 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_relationship_label'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraryitem',
            name='authors',
        ),
        migrations.DeleteModel(
            name='LibraryItemAuthor',
        ),
    ]