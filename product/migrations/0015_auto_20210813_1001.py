# Generated by Django 3.2.4 on 2021-08-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_product_ru',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_product_uk',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='product',
            name='sex_ru',
            field=models.IntegerField(choices=[(0, 'детские'), (1, 'мужские'), (2, 'женские'), (3, 'унисекс')], default=2, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='product',
            name='sex_uk',
            field=models.IntegerField(choices=[(0, 'дитячі'), (1, 'чоловічі'), (2, 'жіночі'), (3, 'унісекс')], default=2, verbose_name='Стать'),
        ),
        migrations.AddField(
            model_name='product',
            name='status_ru',
            field=models.IntegerField(choices=[(0, 'в наличии'), (1, 'нет в наличии'), (2, 'под заказ')], default=0, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='product',
            name='status_uk',
            field=models.IntegerField(choices=[(0, 'в наявності'), (1, 'немає в наявності'), (2, 'під замовлення')], default=0, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sex',
            field=models.IntegerField(choices=[(0, 'children'), (1, 'man'), (2, 'woman'), (3, 'unisex')], default=2, verbose_name='Sex'),
        ),
    ]