# Generated by Django 3.0.3 on 2020-04-20 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_relationship'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='logo',
        ),
        migrations.CreateModel(
            name='UserRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Record')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Relationship')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecordRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='core.Record')),
                ('record_secondary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record_secondary', to='core.Record')),
                ('relationship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Relationship')),
            ],
        ),
    ]
