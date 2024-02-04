# Generated by Django 4.2.4 on 2023-12-23 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('path', models.CharField(db_column='path', default=None, max_length=255, null=True, verbose_name='请求路径')),
                ('component', models.CharField(db_column='component', default=None, max_length=255, null=True, verbose_name='组件')),
                ('redirect', models.CharField(db_column='redirect', default=None, max_length=255, null=True, verbose_name='重定向')),
                ('name', models.CharField(db_column='name', default=None, max_length=255, null=True, verbose_name='名字')),
                ('label', models.CharField(db_column='label', default=None, max_length=255, null=True, verbose_name='标题')),
                ('icon', models.CharField(db_column='icon', default=None, max_length=255, null=True, verbose_name='图标')),
                ('parent_id', models.IntegerField(db_column='parent_id', verbose_name='父节点id 根节点为0')),
                ('status', models.IntegerField(db_column='status', default=1, verbose_name='启用状态 1启用 0禁用')),
                ('perm', models.CharField(db_column='perm', default=None, max_length=255, null=True, verbose_name='权限标识符')),
                ('hidden', models.IntegerField(db_column='hidden', default=None, null=True)),
                ('menu_type', models.CharField(db_column='menu_type', default=None, max_length=255, null=True, verbose_name='m为菜单 f为按钮（接口）')),
                ('order_num', models.IntegerField(db_column='order_num', default=None, null=True, verbose_name='排序')),
                ('remark', models.CharField(db_column='remark', default=None, max_length=255, null=True, verbose_name='备注')),
                ('create_time', models.DateTimeField(db_column='create_time', default=None, null=True)),
                ('update_time', models.DateTimeField(db_column='update_time', default=None, null=True)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='RoleMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.IntegerField()),
                ('menu_id', models.IntegerField()),
            ],
            options={
                'db_table': 'role_menu',
                'unique_together': {('role_id', 'menu_id')},
            },
        ),
    ]
