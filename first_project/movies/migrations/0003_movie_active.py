# Generated by Django 3.2.9 on 2021-11-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211107_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
