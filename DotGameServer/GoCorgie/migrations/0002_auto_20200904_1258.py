# Generated by Django 3.0.4 on 2020-09-04 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoCorgie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
