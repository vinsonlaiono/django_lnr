# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-24 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20180423_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='uploader',
            field=models.ForeignKey(default="0", on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='first_app.User'),
            preserve_default=False,
        ),
    ]