# Generated by Django 3.2.4 on 2021-08-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='product_photo', verbose_name='Photo'),
        ),
    ]
