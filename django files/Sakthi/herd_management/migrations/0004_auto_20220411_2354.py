# Generated by Django 3.2.4 on 2022-04-11 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('herd_management', '0003_auto_20220411_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cattle_records',
            old_name='quality1',
            new_name='quantity1',
        ),
        migrations.RenameField(
            model_name='cattle_records',
            old_name='quality2',
            new_name='quantity2',
        ),
    ]
