# Generated by Django 3.2.4 on 2021-07-05 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='filters.py',
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category'),
        ),
    ]
