# Generated by Django 3.0.3 on 2020-03-12 20:00

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200312_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDesign',
            fields=[
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Article')),
                ('header', models.CharField(choices=[('full', 'Full header with title and subtitle'), ('small', 'Small header; menu only'), ('image', 'Image underneath menu')], default='full', max_length=6)),
                ('header_title', models.CharField(blank=True, max_length=100, null=True)),
                ('header_subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', stdimage.models.StdImageField(blank=True, null=True, upload_to='logos')),
                ('color', models.CharField(blank=True, max_length=14, null=True)),
                ('background', stdimage.models.StdImageField(blank=True, null=True, upload_to='records')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='header',
        ),
        migrations.RemoveField(
            model_name='article',
            name='header_subtitle',
        ),
        migrations.RemoveField(
            model_name='article',
            name='header_title',
        ),
    ]