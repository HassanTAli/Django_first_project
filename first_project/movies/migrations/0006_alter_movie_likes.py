# Generated by Django 3.2.9 on 2021-11-08 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20211108_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
