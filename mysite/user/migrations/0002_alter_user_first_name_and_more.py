# Generated by Django 5.0.6 on 2024-08-13 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='identity_document_type',
            field=models.CharField(blank=True, choices=[('voter_id', 'voter_id'), ('passport', 'passport'), ('citizenship_number', 'citizenship_number')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
