# Generated by Django 3.0.7 on 2020-06-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='cash',
            field=models.IntegerField(default=1000000),
        ),
        migrations.AddField(
            model_name='trader',
            name='positions',
            field=models.TextField(default='{}'),
        ),
    ]
