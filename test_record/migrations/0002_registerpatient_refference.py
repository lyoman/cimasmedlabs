# Generated by Django 2.2.12 on 2020-07-24 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_record', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerpatient',
            name='refference',
            field=models.CharField(default=models.DateTimeField(auto_now_add=True), max_length=200),
        ),
    ]
