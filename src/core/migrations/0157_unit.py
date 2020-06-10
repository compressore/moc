# Generated by Django 3.0.3 on 2020-06-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0156_material_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(1, 'Mass'), (2, 'Volume'), (3, 'Count'), (4, 'Area'), (5, 'Energy'), (6, 'Length'), (7, 'Fraction'), (99, 'Other')], db_index=True, default=99)),
            ],
        ),
    ]
