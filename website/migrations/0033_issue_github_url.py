# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-08 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0032_userprofile_winnings'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='github_url',
            field=models.URLField(default=b''),
        ),
    ]
