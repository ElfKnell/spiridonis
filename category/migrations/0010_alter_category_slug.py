# Generated by Django 3.2.4 on 2021-08-17 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_rename_part_link_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=30, unique=True, verbose_name='Part of the link'),
        ),
    ]
