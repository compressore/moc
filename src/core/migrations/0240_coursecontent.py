# Generated by Django 3.0.6 on 2020-08-05 07:41

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0239_auto_20200805_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Record')),
                ('position', models.PositiveSmallIntegerField(blank=True, db_index=True, null=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='core.CourseModule')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Video')),
            ],
            options={
                'ordering': ['position'],
            },
            bases=('core.record',),
            managers=[
                ('objects_unfiltered', django.db.models.manager.Manager()),
            ],
        ),
    ]