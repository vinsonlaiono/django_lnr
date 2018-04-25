# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-25 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20180424_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quoted_by', models.ManyToManyField(related_name='liked_quotes', to='first_app.User')),
                ('quoter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='first_app.User')),
            ],
        ),
    ]
