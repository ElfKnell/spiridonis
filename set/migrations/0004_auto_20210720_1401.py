# Generated by Django 3.2.4 on 2021-07-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set', '0003_auto_20210719_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='date_create',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='set',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]