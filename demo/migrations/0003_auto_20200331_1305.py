# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-31 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200331_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to=b'covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='book',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
