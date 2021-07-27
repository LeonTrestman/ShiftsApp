# Generated by Django 3.2.5 on 2021-07-27 02:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shifts', '0003_auto_20210727_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklydaydates',
            name='friday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 6, 0, 0)),
        ),
        migrations.AlterField(
            model_name='weeklydaydates',
            name='monday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 2, 0, 0)),
        ),
        migrations.AlterField(
            model_name='weeklydaydates',
            name='saturday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 7, 0, 0)),
        ),
        migrations.AlterField(
            model_name='weeklydaydates',
            name='sunday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 1, 0, 0)),
        ),
        migrations.AlterField(
            model_name='weeklydaydates',
            name='thursday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 0, 0)),
        ),
        migrations.AlterField(
            model_name='weeklydaydates',
            name='tuesday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 3, 0, 0)),
        ),
        migrations.AlterField(
            model_name='weeklydaydates',
            name='wednesday_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 4, 0, 0)),
        ),
    ]