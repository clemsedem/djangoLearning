# Generated by Django 3.0.1 on 2020-01-08 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='ref',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
