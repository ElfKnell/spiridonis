# Generated by Django 3.2.4 on 2021-07-05 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210705_1551'),
        ('attibutes', '0006_attributevariant'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributevariant',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
    ]
