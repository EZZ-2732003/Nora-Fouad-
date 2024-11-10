# Generated by Django 5.1 on 2024-09-10 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('birthday', models.DateField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(default='Default Address', max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField()),
                ('last_visit', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(default='Default Address', max_length=255)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
