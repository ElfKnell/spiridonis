# Generated by Django 3.2.4 on 2021-07-13 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attibutes', '0014_auto_20210713_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributesvalue',
            name='is_variability',
        ),
    ]
