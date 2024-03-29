# Generated by Django 2.2.12 on 2020-07-29 12:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_auto_20200727_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimendata',
            name='daysent',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 7, 29, 12, 37, 7, 436578, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specimendata',
            name='temperature',
            field=models.CharField(default='35', max_length=200),
        ),
        migrations.AddField(
            model_name='specimendata',
            name='weight',
            field=models.CharField(default='60', max_length=200),
        ),
        migrations.AlterField(
            model_name='specimendata',
            name='reff',
            field=models.CharField(default=1596026212869, max_length=200),
        ),
    ]
