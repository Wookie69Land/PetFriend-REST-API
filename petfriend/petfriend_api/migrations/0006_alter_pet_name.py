# Generated by Django 4.1.10 on 2023-08-29 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petfriend_api', '0005_rename_genre_pet_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
