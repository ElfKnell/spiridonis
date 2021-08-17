# Generated by Django 3.2.4 on 2021-08-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_rename_part_link_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=30, unique=True, verbose_name='Part of the link'),
        ),
    ]