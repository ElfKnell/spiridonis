# Generated by Django 3.2.4 on 2021-07-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210702_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company',
        ),
        migrations.AddField(
            model_name='customuser',
            name='company_user',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Company'),
        ),
    ]
