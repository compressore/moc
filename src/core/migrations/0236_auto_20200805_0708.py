# Generated by Django 3.0.6 on 2020-08-05 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0235_course_coursemodule_coursequestion_coursequestionanswer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursequestion',
            options={'ordering': ['position']},
        ),
        migrations.RemoveField(
            model_name='coursequestionanswer',
            name='is_correct',
        ),
        migrations.AddField(
            model_name='coursequestion',
            name='answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.CourseQuestionAnswer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursequestion',
            name='module',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.CourseModule'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursequestion',
            name='position',
            field=models.PositiveSmallIntegerField(blank=True, db_index=True, null=True),
        ),
    ]