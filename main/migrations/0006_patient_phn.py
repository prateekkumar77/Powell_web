# Generated by Django 3.2.3 on 2021-07-02 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_employee_lab_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phn',
            field=models.BigIntegerField(default=0),
        ),
    ]
