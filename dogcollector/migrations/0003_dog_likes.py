# Generated by Django 2.0.3 on 2018-03-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogcollector', '0002_dog_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
