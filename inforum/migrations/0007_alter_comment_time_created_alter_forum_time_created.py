# Generated by Django 4.1 on 2022-10-25 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inforum', '0006_forum_category_alter_comment_time_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 25, 14, 10, 17, 601398, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 25, 14, 10, 17, 600406, tzinfo=datetime.timezone.utc)),
        ),
    ]
