# Generated by Django 3.0.3 on 2020-05-01 04:19

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('stafdb', '0024_auto_20200429_1843'),
        ('core', '0035_auto_20200429_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataViz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', stdimage.models.StdImageField(upload_to='dataviz')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('url', models.CharField(blank=True, help_text='URL of the source website/article -- ONLY enter if this is not linked to a publication', max_length=255, null=True)),
                ('source', models.TextField(blank=True, help_text='Name of the source website/article -- ONLY enter if this is not linked to a publication', null=True)),
                ('year', models.PositiveSmallIntegerField(blank=True, help_text='Year of the data being visualized -- ONLY enter if this is not linked to a publication', null=True)),
                ('reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.LibraryItem')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stafdb.Sector')),
                ('space', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stafdb.ReferenceSpace')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.People')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]