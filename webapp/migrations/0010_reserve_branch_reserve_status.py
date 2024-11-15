# Generated by Django 5.1 on 2024-09-12 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_inventory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='Branch',
            field=models.CharField(choices=[('EL-Mohandsen', 'EL-Mohandsen'), ('5th sattelment', '5th sattelment'), ('Naser-city', 'Naser-city')], default='Branch', max_length=50),
        ),
        migrations.AddField(
            model_name='reserve',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
    ]
