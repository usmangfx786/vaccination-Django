# Generated by Django 5.0.6 on 2024-07-31 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0001_initial'),
        ('vaccine', '0002_rename_vacine_vaccine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_quantity', models.IntegerField(default=0)),
                ('booked_quantity', models.IntegerField(default=0)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.center')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine')),
            ],
        ),
    ]
