# Generated by Django 5.0.6 on 2024-08-07 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0002_rename_vacine_vaccine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vaccine',
            old_name='numbre_of_doses',
            new_name='numbre_of_doses',
        ),
    ]
