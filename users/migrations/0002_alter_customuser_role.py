# Generated by Django 3.2.4 on 2021-06-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.IntegerField(choices=[(1, 'manager'), (2, 'editor')], default=2, null=True),
        ),
    ]
