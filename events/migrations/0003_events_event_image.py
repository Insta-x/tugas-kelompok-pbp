# Generated by Django 4.1 on 2022-10-31 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_delete_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_image',
            field=models.ImageField(default='defaul.jpg', upload_to='images'),
        ),
    ]