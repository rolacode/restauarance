# Generated by Django 4.2.7 on 2023-12-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obe', '0003_remove_menu_full_name_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(),
        ),
    ]
