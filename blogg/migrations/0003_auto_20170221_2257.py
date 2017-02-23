# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='entries',
        ),
        migrations.AddField(
            model_name='entry',
            name='blog',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='blogg.Blog'),
            preserve_default=False,
        ),
    ]