# Generated by Django 3.0.3 on 2020-03-25 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0021_auto_20200326_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
