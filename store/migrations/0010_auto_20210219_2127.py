# Generated by Django 3.1.6 on 2021-02-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210219_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='id',
        ),
        migrations.AlterField(
            model_name='favorite',
            name='favoriteId',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
