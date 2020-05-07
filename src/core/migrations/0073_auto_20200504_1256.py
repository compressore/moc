# Generated by Django 3.0.3 on 2020-05-04 12:56

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_event_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDesign',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='design', serialize=False, to='core.Project')),
                ('header', models.CharField(choices=[('full', 'Full header with title and subtitle'), ('small', 'Small header; menu only'), ('image', 'Image underneath menu')], default='full', max_length=6)),
                ('logo', stdimage.models.StdImageField(blank=True, null=True, upload_to='logos')),
                ('custom_css', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelManagers(
            name='event',
            managers=[
                ('objects_including_deleted', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='webpagedesign',
            name='logo',
        ),
        migrations.AlterField(
            model_name='webpagedesign',
            name='webpage',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Record'),
        ),
    ]