# Generated by Django 3.2.4 on 2021-07-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0007_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sale',
            field=models.IntegerField(default=0),
        ),
    ]
