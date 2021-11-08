# Generated by Django 3.2.9 on 2021-11-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20211108_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='movie/image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(default='', upload_to='movie/videos'),
            preserve_default=False,
        ),
    ]