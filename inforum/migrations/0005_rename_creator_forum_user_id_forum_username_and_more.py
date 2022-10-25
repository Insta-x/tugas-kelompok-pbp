# Generated by Django 4.1 on 2022-10-24 15:19

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inforum', '0004_alter_comment_time_created_alter_forum_time_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forum',
            old_name='creator',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='forum',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 24, 15, 19, 10, 100647, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='forum',
            name='time_created',
            field=models.DateField(default=datetime.datetime(2022, 10, 24, 15, 19, 10, 100647, tzinfo=datetime.timezone.utc)),
        ),
    ]