# Generated by Django 2.2.12 on 2020-07-24 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_record', '0002_registerpatient_refference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerpatient',
            name='refference',
            field=models.CharField(max_length=200),
        ),
    ]
