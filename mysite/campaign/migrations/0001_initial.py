# Generated by Django 5.0.6 on 2024-07-31 06:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('center', '0002_storage'),
        ('vaccine', '0002_rename_vacine_vaccine'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('agents', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='center.center')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccine.vaccine')),
            ],
        ),
    ]
