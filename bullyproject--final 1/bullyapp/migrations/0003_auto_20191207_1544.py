# Generated by Django 2.1 on 2019-12-07 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bullyapp', '0002_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('your_email', models.EmailField(max_length=200)),
                ('date_time_of_incident', models.DateTimeField(default='2019-12-07 15:44:15')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UsernameData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psuStudentUsername', models.CharField(max_length=200)),
                ('psuTeacherUsername', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='content_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 15, 44, 15, 636800), verbose_name='date published'),
        ),
    ]
