# Generated by Django 3.2.4 on 2021-07-02 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_auto_20210701_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_set', models.CharField(max_length=20, unique=True, verbose_name='Set name')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.CharField(max_length=120, verbose_name='Photo')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price')),
                ('opt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Opt price')),
                ('small_opt_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Small opt price')),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Sale price')),
                ('main_product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='product.product')),
                ('product_1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='first', to='product.product')),
                ('product_2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='product.product')),
                ('product_3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third', to='product.product')),
            ],
        ),
    ]
