# Generated by Django 4.2.4 on 2023-12-24 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_mentalmessages_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentalmessages',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
