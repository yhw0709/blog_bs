# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 07:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('修改用户名', 'change_myuser_username'), ('修改密码', 'change_myuser_password'))},
        ),
    ]