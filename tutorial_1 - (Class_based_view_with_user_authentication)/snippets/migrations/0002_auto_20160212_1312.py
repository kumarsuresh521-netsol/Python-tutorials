# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 07:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cms',
            options={'ordering': ('title',)},
        ),
    ]
