# Generated by Django 4.1.10 on 2023-08-29 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petfriend_api', '0004_alter_pet_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='genre',
            new_name='sex',
        ),
    ]
