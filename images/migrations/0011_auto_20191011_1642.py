# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-11 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_auto_20191011_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]
