# Generated by Django 3.0.3 on 2020-04-06 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0025_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='month',
            field=models.CharField(choices=[('Jan', 'Jan'), ('Feb', 'Feb'), ('Mar', 'Mar'), ('Apr', 'Apr'), ('May', 'May'), ('Jun', 'Jun'), ('Jul', 'Jul'), ('Aug', 'Aug'), ('Sep', 'Sep'), ('Oct', 'Oct'), ('Nov', 'Nov'), ('Dec', 'Dec')], default='Mar', max_length=10),
        ),
        migrations.AlterField(
            model_name='fee',
            name='d_date',
            field=models.DateField(default=datetime.date(2020, 4, 6)),
        ),
        migrations.AlterField(
            model_name='fee',
            name='pay_date',
            field=models.DateField(default=datetime.date(2020, 4, 6)),
        ),
        migrations.AlterField(
            model_name='mark',
            name='date',
            field=models.DateField(default=datetime.date(2020, 4, 6)),
        ),
    ]
