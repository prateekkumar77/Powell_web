# Generated by Django 3.2.3 on 2021-06-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210629_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=25)),
                ('age', models.IntegerField(default=1)),
                ('gender', models.CharField(default='', max_length=1)),
            ],
        ),
    ]
