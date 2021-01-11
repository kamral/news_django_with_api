# Generated by Django 3.1.4 on 2021-01-11 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_readers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='readers',
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserNewsRelation',
        ),
    ]
