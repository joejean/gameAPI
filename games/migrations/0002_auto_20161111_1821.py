# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='games',
            old_name='created_at',
            new_name='created',
        ),
    ]
