# Generated by Django 3.1.6 on 2021-02-18 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='productId',
        ),
        migrations.AddField(
            model_name='favorite',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
    ]
