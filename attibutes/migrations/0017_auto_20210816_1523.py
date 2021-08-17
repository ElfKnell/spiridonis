# Generated by Django 3.2.4 on 2021-08-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attibutes', '0016_alter_attributesvalue_name_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='attributes',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='attributes',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='attributes',
            name='name_attributes_ru',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='attributes',
            name='name_attributes_uk',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Назва'),
        ),
        migrations.AddField(
            model_name='attributesvalue',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='attributesvalue',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Опис'),
        ),
        migrations.AddField(
            model_name='attributesvalue',
            name='name_value_ru',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Название значения'),
        ),
        migrations.AddField(
            model_name='attributesvalue',
            name='name_value_uk',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Назва значення'),
        ),
    ]
