# Generated by Django 3.2.4 on 2021-07-06 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attibutes', '0011_auto_20210706_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributevariant',
            name='product',
        ),
    ]
