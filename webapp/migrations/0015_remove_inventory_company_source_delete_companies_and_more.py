# Generated by Django 5.1 on 2024-09-15 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_companies_inventory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='company_source',
        ),
        migrations.DeleteModel(
            name='Companies',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
