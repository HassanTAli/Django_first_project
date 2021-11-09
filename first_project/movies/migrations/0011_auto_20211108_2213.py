# Generated by Django 3.2.9 on 2021-11-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20211108_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AlterModelOptions(
            name='cast',
            options={'ordering': ('first_name',)},
        ),
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.ImageField(upload_to='movie/images'),
        ),
    ]