# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-11-24 18:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comments_timepublish'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='authors',
        ),
        migrations.AlterModelTable(
            name='comments',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
