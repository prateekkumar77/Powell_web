# Generated by Django 3.2.3 on 2021-06-29 11:26

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reports',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('pdf', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to='')),
            ],
        ),
    ]
