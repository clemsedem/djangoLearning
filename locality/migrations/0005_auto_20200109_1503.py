# Generated by Django 3.0.1 on 2020-01-09 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locality', '0004_auto_20200109_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='locality_name',
            field=models.CharField(max_length=20),
        ),
    ]
