# Generated by Django 2.2.12 on 2020-07-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0010_auto_20200729_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimendata',
            name='reff',
            field=models.CharField(default=1596049857345, max_length=200),
        ),
    ]
