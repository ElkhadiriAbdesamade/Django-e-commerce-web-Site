# Generated by Django 3.1.6 on 2021-02-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_customer_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
    ]
