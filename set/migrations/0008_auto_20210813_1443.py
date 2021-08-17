# Generated by Django 3.2.4 on 2021-08-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0007_alter_set_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='set',
            name='description_uk',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='set',
            name='name_set_ru',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Set name'),
        ),
        migrations.AddField(
            model_name='set',
            name='name_set_uk',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Set name'),
        ),
    ]
