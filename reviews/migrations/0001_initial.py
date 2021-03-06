# Generated by Django 3.2.4 on 2021-07-02 11:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_auto_20210701_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Message')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('product', models.ManyToManyField(to='product.Product')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
