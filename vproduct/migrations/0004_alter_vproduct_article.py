# Generated by Django 3.2.4 on 2021-07-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vproduct', '0003_auto_20210706_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vproduct',
            name='article',
            field=models.CharField(max_length=30, verbose_name='Article'),
        ),
    ]
