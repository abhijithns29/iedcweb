# Generated by Django 5.1.2 on 2024-10-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_category_options_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name_plural': 'items'},
        ),
    ]
