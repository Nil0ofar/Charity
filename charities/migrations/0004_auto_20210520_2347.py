# Generated by Django 3.1.7 on 2021-05-20 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charities', '0003_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benefactor',
            old_name='free_Time_per_week',
            new_name='free_time_per_week',
        ),
    ]
