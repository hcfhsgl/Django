# Generated by Django 3.0 on 2023-08-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PictureModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, verbose_name='图片路径')),
                ('name', models.CharField(max_length=255, verbose_name='图片名称')),
                ('size', models.CharField(max_length=255, verbose_name='图片大小')),
            ],
            options={
                'db_table': 'picture',
            },
        ),
    ]
