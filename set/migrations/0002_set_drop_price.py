# Generated by Django 3.2.4 on 2021-07-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='drop_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Sale price'),
        ),
    ]
