# Generated by Django 3.2.4 on 2021-07-06 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vproduct', '0002_auto_20210705_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vproduct',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='vproduct',
            name='product',
        ),
    ]
