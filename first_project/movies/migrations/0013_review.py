# Generated by Django 3.2.9 on 2021-11-08 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20211108_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('attachment', models.FileField(upload_to='movie/review')),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.movie')),
            ],
        ),
    ]
