# Generated by Django 3.0.3 on 2020-03-03 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20200303_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
