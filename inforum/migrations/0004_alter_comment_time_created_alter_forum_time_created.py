# Generated by Django 4.1 on 2022-10-22 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inforum', '0003_alter_comment_time_created_alter_forum_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 22, 16, 33, 52, 485528, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 22, 16, 33, 52, 484504, tzinfo=datetime.timezone.utc)),
        ),
    ]
