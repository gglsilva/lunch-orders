# Generated by Django 4.1 on 2023-09-08 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_delete_menucategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='campany',
            new_name='company',
        ),
    ]
