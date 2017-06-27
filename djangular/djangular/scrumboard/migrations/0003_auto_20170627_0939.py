# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20170627_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='business_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='scrumboard.List'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='card',
            name='story_points',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]