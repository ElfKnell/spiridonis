# Generated by Django 3.2.4 on 2021-07-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attibutes', '0006_attributevariant'),
        ('product', '0007_auto_20210705_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='attribute_variant',
            field=models.ManyToManyField(blank=True, null=True, to='attibutes.AttributeVariant'),
        ),
    ]
