# Generated by Django 3.2.4 on 2021-08-17 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_product_part_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='part_link',
            new_name='slug',
        ),
    ]
