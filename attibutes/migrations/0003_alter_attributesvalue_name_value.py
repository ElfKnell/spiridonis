# Generated by Django 3.2.4 on 2021-07-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attibutes', '0002_attributesvalue_name_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributesvalue',
            name='name_value',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
    ]
