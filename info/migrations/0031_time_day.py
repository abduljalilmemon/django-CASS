# Generated by Django 3.0.3 on 2020-04-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0030_auto_20200409_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='day',
            field=models.CharField(choices=[('Thursday', 'Thursday'), ('Tuesday', 'Tuesday'), ('Friday', 'Friday'), ('Monday', 'Monday'), ('Wednesday', 'Wednesday'), ('Saturday', 'Saturday')], default='Monday', max_length=20),
        ),
    ]