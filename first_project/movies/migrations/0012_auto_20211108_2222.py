# Generated by Django 3.2.9 on 2021-11-08 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20211108_2213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='movie',
            name='casts',
            field=models.ManyToManyField(to='movies.Cast'),
        ),
    ]
