# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-15 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_auto_20171002_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='journal',
            name='domain',
            field=models.CharField(default='www.example.com', max_length=255, unique=True),
        ),
    ]