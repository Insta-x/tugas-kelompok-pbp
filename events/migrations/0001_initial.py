# Generated by Django 4.1 on 2022-10-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_image', models.ImageField(upload_to='img')),
                ('event_type', models.CharField(max_length=20)),
                ('event_title', models.CharField(max_length=50)),
                ('developer', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('schedule', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
