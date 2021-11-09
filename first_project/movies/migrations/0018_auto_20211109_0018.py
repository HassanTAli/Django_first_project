# Generated by Django 3.2.9 on 2021-11-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='id',
            name='name',
        ),
        migrations.AddField(
            model_name='id',
            name='number',
            field=models.IntegerField(default=5, max_length=150),
            preserve_default=False,
        ),
    ]
