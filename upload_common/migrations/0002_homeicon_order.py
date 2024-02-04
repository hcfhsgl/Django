# Generated by Django 4.2.4 on 2023-08-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeIcon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'home_icon',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple', models.IntegerField()),
                ('vivo', models.IntegerField()),
                ('oppo', models.IntegerField()),
                ('meizu', models.IntegerField()),
                ('samsung', models.IntegerField()),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
