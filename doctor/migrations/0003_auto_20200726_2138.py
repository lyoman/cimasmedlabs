# Generated by Django 2.2.12 on 2020-07-26 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_specimendata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specimendata',
            name='reff',
            field=models.CharField(default=1595792303082, max_length=200),
        ),
    ]